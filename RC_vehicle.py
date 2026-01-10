import time
from fischertechnik.controller.Motor import Motor
from lib.controller import *
from lib.Math_lib import *
from lib.RC_lib import *

Speed = None
Values_read = None
Lights_on = None
prev_buttonLB = None
Reverse_on = None
Analog = None
prev_buttonRB = None
Buttons = None
Axes = None


def Toggle_headlights():
  global Speed, Values_read, Lights_on, prev_buttonLB, Reverse_on, Analog, prev_buttonRB, Buttons, Axes
  if Buttons['LB'] and not prev_buttonLB:
    Lights_on = not Lights_on
    TXT_M_O7_led.set_brightness(int(512 if Lights_on else 0))
    TXT_M_O5_led.set_brightness(int(100 if Lights_on else 0))
  prev_buttonLB = Buttons['LB']


def Throttle():
  global Speed, Values_read, Lights_on, prev_buttonLB, Reverse_on, Analog, prev_buttonRB, Buttons, Axes
  Speed = Analog['Throttle'] * 0.5


def Init():
  global Speed, Values_read, Lights_on, prev_buttonLB, Reverse_on, Analog, prev_buttonRB, Buttons, Axes
  Speed = 0
  Reverse_on = False
  prev_buttonRB = False
  prev_buttonLB = False
  Lights_on = False


def Steer():
  global Speed, Values_read, Lights_on, prev_buttonLB, Reverse_on, Analog, prev_buttonRB, Buttons, Axes
  TXT_M_S1_servomotor.set_position(int(Axes['X'] * 0.5))


def Toggle_reverse():
  global Speed, Values_read, Lights_on, prev_buttonLB, Reverse_on, Analog, prev_buttonRB, Buttons, Axes
  if Buttons['RB'] and not prev_buttonRB:
    Reverse_on = not Reverse_on
    TXT_M_O8_led.set_brightness(int(512 if Reverse_on else 0))
  if Reverse_on:
    TXT_M_M1_motor.set_speed(int(Speed), Motor.CCW)
    TXT_M_M1_motor.start()
  else:
    TXT_M_M1_motor.set_speed(int(Speed), Motor.CW)
    TXT_M_M1_motor.start()
  prev_buttonRB = Buttons['RB']


def Honk():
  global Speed, Values_read, Lights_on, prev_buttonLB, Reverse_on, Analog, prev_buttonRB, Buttons, Axes
  if Buttons['B'] == True:
    TXT_M_O6_buzzer.on()
  else:
    TXT_M_O6_buzzer.off()


def Read_values():
  global Speed, Values_read, Lights_on, prev_buttonLB, Reverse_on, Analog, prev_buttonRB, Buttons, Axes
  Values_read = Read_RC()
  Analog = Read_analog_buttons(Values_read)
  Buttons = Read_buttons(Values_read)
  Axes = Read_axes(Values_read)


Init_RC()
Init()
while True:
  if TXT_M_I1_mini_switch.is_closed():
    Write_RC('r', [255, 50])
  Read_values()
  Throttle()
  Steer()
  Toggle_headlights()
  Toggle_reverse()
  Honk()
  time.sleep(0.02)
