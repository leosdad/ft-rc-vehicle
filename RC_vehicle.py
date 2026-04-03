"""
RC vehicle main program.
"""

import time
from fischertechnik.controller.Motor import Motor
from lib.controller import *
from lib.Math_lib import *
from lib.RC_lib import *


# Must review these (ROBO Pro Coding just *loves* global variables...)
Speed = None
Values_read = None
Lights_on = None
prev_buttonLB = None
Reverse_on = None
Analog = None
prev_buttonRB = None
Buttons = None
Axes = None
steering = None
Steer_position = None
Steer_full_lock_ms = None
Steer_last_time = None
Steer_motor_speed = None
Steer_motor_min_speed = None
Steer_deadband = None
Steer_positive_direction = None
Steer_negative_direction = None
Steer_center_search_time = None
Steer_centered = None


def Init():
  """Initialize variables."""
  global Speed, Lights_on, prev_buttonLB, Reverse_on, prev_buttonRB
  global steering, Steer_position, Steer_full_lock_ms, Steer_last_time
  global Steer_motor_speed, Steer_motor_min_speed, Steer_deadband, Steer_positive_direction
  global Steer_negative_direction, Steer_center_search_time, Steer_centered
  Speed = 0
  Reverse_on = False
  prev_buttonRB = False
  prev_buttonLB = False
  Lights_on = False
  steering = "motor"
  Steer_position = 0
  Steer_full_lock_ms = 500  # ms from center to full lock at Steer_motor_min_speed; measure and tune
  Steer_last_time = time.monotonic()
  Steer_motor_speed = Motor.MAX_SPEED
  Steer_motor_min_speed = 300
  Steer_deadband = 4
  Steer_positive_direction = Motor.CCW
  Steer_negative_direction = Motor.CW
  Steer_center_search_time = 1.5
  Steer_centered = True
  ResetSteering()


def Center_steer_motor():
  """Home the steering motor using the center switch."""
  global Steer_position, Steer_centered
  if center_switch.is_closed():
    steer_motor.stop()
    Steer_position = 0
    Steer_centered = True
    return

  Steer_centered = False
  steer_motor.set_speed(Steer_motor_min_speed, Steer_positive_direction)
  steer_motor.start()
  start_time = time.monotonic()
  while not center_switch.is_closed() and time.monotonic() - start_time < Steer_center_search_time:
    time.sleep(0.005)

  if not center_switch.is_closed():
    steer_motor.set_speed(Steer_motor_min_speed, Steer_negative_direction)
    steer_motor.start()
    while not center_switch.is_closed():
      time.sleep(0.005)

  steer_motor.stop()
  Steer_position = 0
  Steer_centered = True


def Toggle_headlights():
  """Toggle the vehicle headlightswhen the left bumper (LB) is pressed."""
  global Lights_on, prev_buttonLB
  if Buttons['LB'] and not prev_buttonLB:
    Lights_on = not Lights_on
    headlights_led.set_brightness(int(512 if Lights_on else 0))
    taillights_led.set_brightness(int(100 if Lights_on else 0))
  prev_buttonLB = Buttons['LB']


def Throttle():
  """Set the throttle based on the RC input."""
  global Speed
  Speed = min(512, max(0, Analog['Throttle'] * 0.5))


def Steer():
  """Set the steering based on the RC input."""
  global Steer_position, Steer_centered, Steer_last_time
  if steering == "servo":
    steer_servo.set_position(int(Axes['X'] * 0.5))
    return

  now = time.monotonic()
  dt_ms = (now - Steer_last_time) * 1000
  Steer_last_time = now

  if center_switch.is_closed():
    Steer_position = 0
    Steer_centered = True

  if not Steer_centered:
    return

  joystick = Axes['X'] - 256  # -256..+256
  target = joystick * Steer_full_lock_ms / 256  # ±Steer_full_lock_ms

  if abs(joystick) <= Steer_deadband:
    if center_switch.is_closed():
      steer_motor.stop()
      Steer_position = 0
    elif Steer_position > 0:
      steer_motor.set_speed(Steer_motor_min_speed, Steer_negative_direction)
      steer_motor.start()
      Steer_position = max(1, Steer_position - dt_ms)
    elif Steer_position < 0:
      steer_motor.set_speed(Steer_motor_min_speed, Steer_positive_direction)
      steer_motor.start()
      Steer_position = min(-1, Steer_position + dt_ms)
    return

  error = target - Steer_position
  if abs(error) < dt_ms:
    steer_motor.stop()
    return

  speed = min(
    Steer_motor_speed,
    max(
      Steer_motor_min_speed,
      int(Steer_motor_min_speed + abs(joystick) * (Steer_motor_speed - Steer_motor_min_speed) / 256)
    )
  )
  advance = dt_ms * speed / Steer_motor_min_speed

  if error > 0:
    steer_motor.set_speed(speed, Steer_positive_direction)
    steer_motor.start()
    Steer_position = min(target, Steer_position + advance)
  else:
    steer_motor.set_speed(speed, Steer_negative_direction)
    steer_motor.start()
    Steer_position = max(target, Steer_position - advance)


def ResetSteering():
  """Center the steering servo."""
  if steering == "motor":
    Center_steer_motor()
  else:
    steer_motor.stop()
    steer_servo.set_position(256)


def Toggle_reverse():
  """Toggle the vehicle reverse mode when the right bumper (RB) is pressed."""
  global Reverse_on, prev_buttonRB
  if Buttons['RB'] and not prev_buttonRB:
    Reverse_on = not Reverse_on
    reverse_led.set_brightness(int(512 if Reverse_on else 0))
  if Reverse_on:
    drive_motor.set_speed(int(Speed), Motor.CCW)
    drive_motor.start()
  else:
    drive_motor.set_speed(int(Speed), Motor.CW)
    drive_motor.start()
  prev_buttonRB = Buttons['RB']


def Honk():
  """Activate the horn when the B button is pressed."""
  if Buttons['B']:
    horn_buzzer.on()
  else:
    horn_buzzer.off()


def Read_RC_values():
  """Read values from the RC controller and update global variables."""
  global Values_read, Analog, Buttons, Axes
  Values_read = Read_RC()
  Analog = Read_analog_buttons(Values_read)
  Buttons = Read_buttons(Values_read)
  Axes = Read_axes(Values_read)


# Main code

Init_RC()
Init()
while True:
  Read_RC_values()
  Throttle()
  Steer()
  Toggle_headlights()
  Toggle_reverse()
  Honk()
  time.sleep(0.02)
