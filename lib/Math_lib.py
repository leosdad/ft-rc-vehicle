
values = None
index = None
value = None


def Unpack4_signed(values, index):
  global value
  import struct

  # Convert 4 bytes into a signed 32-bit integer (little-endian)
  return struct.unpack("<i", bytearray(values[index:(index + 4)]))[0]



def Unpack2_unsigned(values, index):
  global value
  import struct

  return struct.unpack("<H", bytearray(values[index:(index + 2)]))[0]



def Center_0_512(value):
  global values, index
  import fischertechnik.utility.math as ft_math

  return min(512, max(0, ft_math.map(value, -511, 512, 0, 512)))
