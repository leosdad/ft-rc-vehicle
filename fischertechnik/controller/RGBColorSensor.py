#!/usr/bin/python
# -*- coding: UTF-8 -*-
from .I2C import I2C
from .BaseController import BaseController
from typing import List


class RGBColorSensor(I2C):
    def __init__(self, controller: BaseController, identifier: int):
        """The class constructor

        Args:
            controller (BaseController): The controller
            identifier (int): The dentifier
        """
        I2C.__init__(self, controller, identifier)

    def set_auto_off_light(self, t: int):
        """Sets the automatic shutdown of the LED lighting for all sensors.

        Args:
            t (int): The time in seconds (0 = no auto off)
        """
        pass

    def set_cycle_counter(self, c: int):
        """Sets cycle counter to check the timeliness of the measured values.

        Args:
            c (int): The cycle counter
        """
        pass

    def set_measurement_time(self, idx: int, mt: int):
        """Sets the measurement time for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)
            mt (int): The measurement time
        """
        pass

    def set_led_brightness(self, idx: int, pwm: int, led = -1):
        """Sets the brightness for one or all LEDs on a specific sensor.

        Args:
            idx (int): The sensor index (0-7)
            pwm (int): The brightness
            led (int, optional): The LED index (0-2), default is -1 for all LEDs
        """
        pass

    def set_led_on(self, idx: int, led = -1):
        """Turns on one or all LEDs on a specific sensor.

        Args:
            idx (int): The sensor index (0-7)
            led (int, optional): The LED index (0-2), default is -1 for all LEDs
        """
        pass

    def set_led_off(self, idx: int, led = -1):
        """Turns off one or all LEDs on a specific sensor.

        Args:
            idx (int): The sensor index (0-7)
            led (int, optional): The LED index (0-2), default is -1 for all LEDs
        """
        pass

    def is_led_on(self, idx: int, led: int) -> bool:
        """Returns whether one of the three LEDs is on or not.

        Args:
            idx (int): The sensor index (0-7)
            led (int): The LED index (0-2)

        Returns:
            bool: True for on, False otherwise
        """
        pass

    def is_led_off(self, idx: int, led: int) -> bool:
        """Returns whether one of the three LEDs is off or not.

        Args:
            idx (int): The sensor index (0-7)
            led (int): The LED index (0-2)

        Returns:
            bool: True for off, False otherwise
        """
        pass

    def get_firmware_version(self) -> str:
        """Returns the master sensor firmware version.

        Returns:
            str: The firmware version
        """
        pass

    def get_sensor_count(self) -> int:
        """Returns the number of connected sensors.

        Returns:
            int: The number of sensors
        """
        pass

    def get_auto_off_light(self) -> int:
        """Returns the automatic shutdown time of the LED lighting for all sensors.

        Returns:
            int: The automatic shutdown time
        """
        pass

    def get_measurement_time(self, idx: int) -> int:
        """Returns the current measurement time for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            int: The measurement time
        """
        pass

    def get_current_measurement_time(self, idx: int) -> int:
        """Returns the current measurement time to determine the values for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            int: The time of measurement in the sensor (ms)
        """
        pass

    def get_cycle_counter(self, idx: int) -> int:
        """Returns the cycle counter for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            int: The cycle counter
        """
        pass

    def get_led_brightness(self, idx: int, led: int) -> int:
        """Returns the brightness for one of the 3 LEDs for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)
            led (int): The LED index (0-2)

        Returns:
            int: The brightness
        """
        pass

    def get_rgb_red(self, idx: int) -> int:
        """Returns the red value of the RGB color for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            int: The red value (0 - 65535)
        """
        pass

    def get_rgb_green(self, idx: int) -> int:
        """Returns the green value of the RGB color for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            int: The green value (0 - 65535)
        """
        pass

    def get_rgb_blue(self, idx: int) -> int:
        """Returns the blue value of the RGB color for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            int: The blue value (0 - 65535)
        """
        pass

    def get_rgb(self, idx: int) -> List[int]:
        """Returns the RGB color for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            List[int]: The RGB color
        """
        pass

    def get_hsv_hue(self, idx: int) -> int:
        """Returns the hue of the HSV color for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            int: The hue (0 - 360)
        """
        pass

    def get_hsv_saturation(self, idx: int) -> int:
        """Returns the saturation of the HSV color for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            int: The saturation (0 - 100)
        """
        pass

    def get_hsv_value(self, idx: int) -> int:
        """Returns the brightness (value) of the HSV color for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            int: The brightness (0 - 100)
        """
        pass

    def get_hsv(self, idx: int) -> List[int]:
        """Returns the HSV color for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            List[int]: The HSV color
        """
        pass

    def get_hex(self, idx: int) -> str:
        """Returns the HEX color for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            str: The HEX color
        """
        pass

    def get_white_value(self, idx: int) -> int:
        """Returns the white value for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            int: The ambient light (0 - 65535)
        """
        pass
