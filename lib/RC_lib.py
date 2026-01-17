"""
Library for interfacing with the RC module over I2C.
"""

# Must review these (ROBO Pro Coding just *loves* global variables...)

from contextlib import closing
import smbus
from smbus2 import SMBus
from lib.Math_lib import Unpack2_unsigned, Unpack4_signed, Center_0_512

bus = None
controller_index = None
rc_module_address = None

# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
# pylint: disable=missing-function-docstring
# pylint: disable=global-statement

def Detect_I2C_devices():
  # https://chatgpt.com/c/686aaa1f-3f54-8002-8c7a-afe11eec7ded

  def i2c_scan(bus_number=3):
    found = []
    for addr in range(0x03, 0x78):
      try:
        with closing(SMBus(bus_number)) as scan_bus:
          scan_bus.read_byte(addr)
        found.append(addr)
      except OSError:
        pass
    return found

  print("Detected I2C addresses:", [hex(a) for a in i2c_scan()])


def Init_RC():
  global bus, rc_module_address, controller_index
  controller_index = 0
  rc_module_address = 0x28
  bus = smbus.SMBus(3)
  # Device initialization goes here
  # bus.write_byte_data(rc_module_address, ...


def Read_buttons(values):
  # Refer to GamepadState struct in the ESP32 sketch

  buttons = values[2] + (values[3]) << 8

  return {
    'A': buttons & 0x100 == 0x100,
  	'B': buttons & 0x200 == 0x200,
  	'X': buttons & 0x400 == 0x400,
  	'Y': buttons & 0x800 == 0x800,
  	'LB': buttons & 0x1000 == 0x1000,
  	'RB': buttons & 0x2000 == 0x2000,
  	'LT': buttons & 0x4000 == 0x4000,
  	'RT': buttons & 0x8000 == 0x8000
  }


def Read_controller_index(values):
  # Refer to GamepadState struct in the ESP32 sketch

  global controller_index
  controller_index = values[0]
  return values[0]


def Read_DPad(values):
  # Refer to GamepadState struct in the ESP32 sketch

  return {
      'Up':    values[1] & 0x01 == 0x01,
      'Down': values[1] & 0x02 == 0x02,
      'Right':  values[1] & 0x04 == 0x04,
      'Left':  values[1] & 0x08 == 0x08
  }


def Read_analog_buttons(values):
  return {
    'Brake': Unpack2_unsigned(values, 20),
  	'Throttle': Unpack2_unsigned(values, 24),
  	'Misc': (values[24] + values[25]) << 8
  }


def Write_RC(cmd, data):
  # https://chatgpt.com/c/6871912e-f378-8002-a959-6a6c9740ad41

  cmd_byte = ord(cmd) if isinstance(cmd, str) else cmd

  if isinstance(data, int):
    data = [data]
  elif data is None:
    data = []
  elif not all(0 <= b <= 255 for b in data):
    raise ValueError("Invalid data bytes")

  payload = [controller_index, cmd_byte] + data
  # print(payload)

  try:
    bus.write_i2c_block_data(rc_module_address, payload[0], payload[1:])
  except OSError as e:
    print("I2C write failed:", e)


def Read_RC():
  try:
    return bus.read_i2c_block_data(rc_module_address, 0, 32)
  except OSError as e:
    print("Try resetting the ESP32 or reconnect the I2C cable.")
    print("I2C read failed:", e)
    return [0] * 32  # Return a default value on error


def Read_axes(values):
  """Axes are mapped to 0-512."""
  return {
  	'X':  Center_0_512(Unpack4_signed(values, 4)),
  	'Y':  Center_0_512(Unpack4_signed(values, 8)),
  	'RX': Center_0_512(Unpack4_signed(values, 12)),
  	'RY': Center_0_512(Unpack4_signed(values, 16))
  }
