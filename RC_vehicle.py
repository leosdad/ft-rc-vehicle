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


def Init():
  """Initialize variables."""
  global Speed, Lights_on, prev_buttonLB, Reverse_on, prev_buttonRB
  Speed = 0
  Reverse_on = False
  prev_buttonRB = False
  prev_buttonLB = False
  Lights_on = False


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
  steer_servo.set_position(int(Axes['X'] * 0.5))


def ResetSteering():
  """Center the steering servo."""
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
