from apds9960.const import *
from apds9960 import APDS9960
from smbus import SMBus
from typing import List

import colorsys
import threading
import time

from ...models.Color import Color
from ..GestureSensor import GestureSensor

class Txt4GestureSensor(GestureSensor):

    def __init__(self, controller, identifier):
        GestureSensor.__init__(self, controller, identifier)
        self.__apds = APDS9960(SMBus(3))
        self.__lock = threading.Lock()
        self.__thread = None
        self.__gesture = APDS9960_DIR_NONE
        self.__last_gesture_time = time.time()

    def enable_light(self):
        """Start the light (R/G/B/Ambient) sensor.
        """
        self.__apds.enableLightSensor()

    def disable_light(self):
        """Stop the light sensor.
        """
        self.__apds.disableLightSensor()

    def get_rgb_red(self) -> int:
        """Returns the red value of the RGB color.

        Returns:
            int: The red value
        """
        return self.get_rgb()[0]

    def get_rgb_green(self) -> int:
        """Returns the green value of the RGB color.

        Returns:
            int: The green value
        """
        return self.get_rgb()[1]

    def get_rgb_blue(self) -> int:
        """Returns the blue value of the RGB color.

        Returns:
            int: The blue value
        """
        return self.get_rgb()[2]

    def get_rgb(self) -> List[int]:
        """Returns the RGB color of the sensor.

        Returns:
            List[int]: The RGB color
        """
        r = self.__apds.readRedLight()
        if r is None:
            r = -1

        g = self.__apds.readGreenLight()
        if g is None:
            g = -1

        b = self.__apds.readBlueLight()
        if b is None:
            b = -1

        return [r, g, b]

    def get_hsv_hue(self) -> int:
        """Returns the hue of the HSV color.

        Returns:
            int: The hue (0 - 360)
        """
        return self.get_hsv()[0]

    def get_hsv_saturation(self) -> int:
        """Returns the saturation of the HSV color.

        Returns:
            int: The saturation (0 - 100)
        """
        return self.get_hsv()[1]

    def get_hsv_value(self) -> int:
        """Returns the brightness (value) of the HSV color.

        Returns:
            int: The brightness (0 - 100)
        """
        return self.get_hsv()[2]

    def get_hsv(self) -> List[int]:
        """Returns the HSV color of the sensor.

        Returns:
            List[int]: The HSV color
        """
        ambient = self.get_ambient()
        if ambient == 0:
            ambient = 1
        h, s, v = colorsys.rgb_to_hsv(
            self.get_rgb_red() / ambient,
            self.get_rgb_green() / ambient,
            self.get_rgb_blue() / ambient
        )
        return [int(h * 360), int(s * 100), int(v * 100)]

    def get_hex(self) -> str:
        """Returns the HEX color of the sensor.

        Returns:
            str: The HEX color
        """
        hsv = self.get_hsv()
        r, g, b = colorsys.hsv_to_rgb(hsv[0] / 360, hsv[1] / 100, hsv[2] / 100)
        return "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))

    def get_ambient(self) -> int:
        """Returns the ambient light of the sensor.

        Returns:
            int: The ambient light
        """
        ambient = self.__apds.readAmbientLight()
        if ambient is not None:
            return ambient
        return -1

    def enable_proximity(self, threshold = 50):
        """Start the proximity sensor.

        Args:
            threshold (int, optional): Low threshold value for interrupt to trigger. Defaults to 50.
        """
        self.__apds.setProximityIntLowThreshold(threshold)
        self.__apds.enableProximitySensor()

    def disable_proximity(self):
        """Stop the proximity sensor.
        """
        self.__apds.disableProximitySensor()

    def get_proximity(self) -> int:
        """Returns the proximity level as an 8-bit value.

        Returns:
            int: The proximity
        """
        proximity = self.__apds.readProximity()
        if proximity is not None:
            return proximity
        return -1

    def enable_gesture(self, threshold = 50):
        """Start the gesture recognition engine.

        Args:
            threshold (int, optional): Low threshold value for interrupt to trigger. Defaults to 50.
        """
        self.__apds.setProximityIntLowThreshold(threshold)
        self.__apds.enableGestureSensor()
        self.__start_read_gesture()

    def disable_gesture(self):
        """Stop the gesture recognition engine.
        """
        self.__stop_read_gesture()
        self.__apds.disableGestureSensor()

    def get_gesture(self) -> int:
        """Returns best guessed gesture.

        Returns:
            int: The gesture
        """
        if self.__gesture is not None:
            return self.__gesture
        return -1

    def __start_read_gesture(self):
        self.__stop_read_gesture()
        self.__running = True
        self.__thread = threading.Thread(target=self.__read_gesture, args=(), daemon=True)
        self.__thread.start()

    def __stop_read_gesture(self):
        self.__running = False
        if self.__thread is not None:
            self.__thread.join()
            self.__thread = None

    def __read_gesture(self):
        while self.__running:
            if self.__apds.isGestureAvailable():
                with self.__lock:
                    self.__gesture = self.__apds.readGesture()
                    self.__last_gesture_time = time.time()
            else:
                current_time = time.time()
                if (current_time - self.__last_gesture_time) > 0.7:
                    with self.__lock:
                        self.__gesture = APDS9960_DIR_NONE

