#!/usr/bin/python
# -*- coding: UTF-8 -*-
from .I2C import I2C
from .BaseController import BaseController
from typing import List


class GestureSensor(I2C):
    def __init__(self, controller: BaseController, identifier: int):
        """The class constructor

        Args:
            controller (BaseController): The controller
            identifier (int): The dentifier
        """
        I2C.__init__(self, controller, identifier)

    def enable_light(self):
        """Start the light (R/G/B/Ambient) sensor.
        """
        pass

    def disable_light(self):
        """Stop the light sensor.
        """
        pass

    def get_rgb_red(self) -> int:
        """Returns the red value of the RGB color.

        Returns:
            int: The red value
        """
        pass

    def get_rgb_green(self) -> int:
        """Returns the green value of the RGB color.

        Returns:
            int: The green value
        """
        pass

    def get_rgb_blue(self) -> int:
        """Returns the blue value of the RGB color.

        Returns:
            int: The blue value
        """
        pass

    def get_rgb(self) -> List[int]:
        """Returns the RGB color of the sensor.

        Returns:
            List[int]: The RGB color
        """
        pass

    def get_hsv_hue(self) -> int:
        """Returns the hue of the HSV color.

        Returns:
            int: The hue (0 - 360)
        """
        pass

    def get_hsv_saturation(self) -> int:
        """Returns the saturation of the HSV color.

        Returns:
            int: The saturation (0 - 100)
        """
        pass

    def get_hsv_value(self) -> int:
        """Returns the brightness (value) of the HSV color.

        Returns:
            int: The brightness (0 - 100)
        """
        pass

    def get_hsv(self) -> List[int]:
        """Returns the HSV color of the sensor.

        Returns:
            List[int]: The HSV color
        """
        pass

    def get_hex(self) -> str:
        """Returns the HEX color of the sensor.

        Returns:
            str: The HEX color
        """
        pass

    def get_ambient(self) -> int:
        """Returns the ambient light of the sensor.

        Returns:
            int: The ambient light
        """
        pass

    def enable_gesture(self, threshold = 50):
        """Start the gesture recognition engine.

        Args:
            threshold (int, optional): Low threshold value for interrupt to trigger. Defaults to 50.
        """
        pass

    def enable_proximity(self, threshold = 50):
        """Start the proximity sensor.

        Args:
            threshold (int, optional): Low threshold value for interrupt to trigger. Defaults to 50.
        """
        pass

    def disable_proximity(self):
        """Stop the proximity sensor.
        """
        pass

    def get_proximity(self) -> int:
        """Returns the proximity level as an 8-bit value.

        Returns:
            int: The proximity
        """
        pass

    def disable_gesture(self):
        """Stop the gesture recognition engine.
        """
        pass

    def get_gesture(self) -> int:
        """Returns best guessed gesture.

        Returns:
            int: The gesture
        """
        pass

