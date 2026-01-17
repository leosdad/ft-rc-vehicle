"""Mathematical helper functions for the RC library."""

# Imports
import struct
import fischertechnik.utility.math as ft_math

def Unpack4_signed(values, index):
  """Convert 4 bytes into a signed 32-bit integer (little-endian)."""
  return struct.unpack("<i", bytearray(values[index:(index + 4)]))[0]


def Unpack2_unsigned(values, index):
  """Convert 2 bytes into an unsigned 16-bit integer (little-endian)."""
  return struct.unpack("<H", bytearray(values[index:(index + 2)]))[0]


def Center_0_512(value):
  """Map value from -511..512 to 0..512 and clamp."""
  return min(512, max(0, ft_math.map(value, -511, 512, 0, 512)))
