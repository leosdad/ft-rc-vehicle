import smbus2
import colorsys
from typing import List
from ..RGBColorSensor import RGBColorSensor


class ADDRESS(object):
    RGB = 0x14

class REGISTER(object):
    ANZ_SENSOREN = 0x10
    FW_VERSION = 0x11
    SET_CYCLE_COUNTER = 0x18
    SET_AUTO_OFF_LIGHT = 0x19
    GET_COLOR_X = 0x20
    INIT_SENSOR_X = 0x40

class Txt4RGBColorSensor(RGBColorSensor):

    def __init__(self, controller, identifier):
        RGBColorSensor.__init__(self, controller, identifier)
        self.__i2c = smbus2.SMBus(3)
        self.__sensor_test()
        self.__mtx = [2] * 8
        self.__pwm = [[128] * 3] * 8
        self.__auto_off_time = 0

    def set_auto_off_light(self, t: int):
        """Sets the automatic shutdown of the LED lighting for all sensors.

        Args:
            t (int): The time in seconds (0 = no auto off)
        """
        self.__auto_off_time = t
        self.__i2c.write_byte_data(ADDRESS.RGB, REGISTER.SET_AUTO_OFF_LIGHT, self.__auto_off_time)

    def set_cycle_counter(self, c: int):
        """Sets cycle counter to check the timeliness of the measured values.

        Args:
            c (int): The cycle counter
        """
        self.__i2c.write_byte_data(ADDRESS.RGB, REGISTER.SET_CYCLE_COUNTER, c)

    def set_measurement_time(self, idx: int, mt: int):
        """Sets the measurement time for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)
            mt (int): The measurement time
        """
        self.__init_sensor(idx, mt, self.__pwm[idx][0], self.__pwm[idx][1], self.__pwm[idx][2])

    def set_led_brightness(self, idx: int, pwm: int, led = -1):
        """Sets the brightness for one or all LEDs on a specific sensor.

        Args:
            idx (int): The sensor index (0-7)
            pwm (int): The brightness
            led (int, optional): The LED index (0-2), default is -1 for all LEDs

        Raises:
            ValueError: If the brightness is less than 0 or greater than 255
        """
        if pwm < 0 or pwm > 255:
            raise ValueError("Brightness must be >=0 and <=255")

        if led >= 0 and led <=2:
            self.__pwm[idx][led] = pwm
        else:
            self.__pwm[idx][0] = pwm
            self.__pwm[idx][1] = pwm
            self.__pwm[idx][2] = pwm

        self.__init_sensor(idx, self.__mtx[idx], self.__pwm[idx][0], self.__pwm[idx][1], self.__pwm[idx][2])

    def set_led_on(self, idx: int, led = -1):
        """Turns on one or all LEDs on a specific sensor.

        Args:
            idx (int): The sensor index (0-7)
            led (int, optional): The LED index (0-2), default is -1 for all LEDs
        """
        self.set_led_brightness(idx, 255, led)

    def set_led_off(self, idx: int, led = -1):
        """Turns off one or all LEDs on a specific sensor.

        Args:
            idx (int): The sensor index (0-7)
            led (int, optional): The LED index (0-2), default is -1 for all LEDs
        """
        self.set_led_brightness(idx, 0, led)

    def is_led_on(self, idx: int, led: int) -> bool:
        """Returns whether one of the three LEDs is on or not.

        Args:
            idx (int): The sensor index (0-7)
            led (int): The LED index (0-2)

        Returns:
            bool: True for on, False otherwise
        """
        return self.get_led_brightness(idx, led) > 0

    def is_led_off(self, idx: int, led: int) -> bool:
        """Returns whether one of the three LEDs is off or not.

        Args:
            idx (int): The sensor index (0-7)
            led (int): The LED index (0-2)

        Returns:
            bool: True for off, False otherwise
        """
        return self.get_led_brightness(idx, led) <= 0

    def get_firmware_version(self) -> str:
        """Returns the master sensor firmware version.

        Returns:
            str: The firmware version
        """
        result = self.__i2c.read_i2c_block_data(ADDRESS.RGB, REGISTER.FW_VERSION, 2)
        if result is not None:
            return '{}.{}'.format(str(result[1]), str(result[0]))
        return '0.0'

    def get_sensor_count(self) -> int:
        """Returns the number of connected sensors.

        Returns:
            int: The number of sensors
        """
        result = self.__i2c.read_i2c_block_data(ADDRESS.RGB, REGISTER.ANZ_SENSOREN, 1)
        if result is not None:
            return result[0]
        return -1

    def get_auto_off_light(self) -> int:
        """Returns the automatic shutdown time of the LED lighting for all sensors.

        Returns:
            int: The automatic shutdown time
        """
        return self.__auto_off_time

    def get_measurement_time(self, idx: int) -> int:
        """Returns the set measurement time to determine the values for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            int: The measurement time
        """
        return self.__mtx[idx]

    def get_current_measurement_time(self, idx: int) -> int:
        """Returns the current measurement time for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            int: The time of measurement in the sensor (ms)
        """
        result = self.__read_color(idx)
        if result is not None:
            return 256 * result[10] + result[9]
        return -1

    def get_cycle_counter(self, idx: int) -> int:
        """Returns the cycle counter for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            int: The cycle counter
        """
        result = self.__read_color(idx)
        if result is not None:
            return result[0]
        return -1

    def get_led_brightness(self, idx: int, led: int) -> int:
        """Returns the brightness for one of the 3 LEDs for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)
            led (int): The LED index (0-2)

        Returns:
            int: The brightness
        """
        return self.__pwm[idx][int(led)]

    def get_rgb_red(self, idx: int) -> int:
        """Returns the red value of the RGB color for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            int: The red value (0 - 65535)
        """
        return self.get_rgb(idx)[0]

    def get_rgb_green(self, idx: int) -> int:
        """Returns the green value of the RGB color for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            int: The green value (0 - 65535)
        """
        return self.get_rgb(idx)[1]

    def get_rgb_blue(self, idx: int) -> int:
        """Returns the blue value of the RGB color for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            int: The blue value (0 - 65535)
        """
        return self.get_rgb(idx)[2]

    def get_rgb(self, idx: int) -> List[int]:
        """Returns the RGB color for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            List[int]: The RGB color
        """
        result = self.__read_color(idx)
        if result is not None:
            return [
                256 * result[2] + result[1],
                256 * result[4] + result[3],
                256 * result[6] + result[5]
            ]
        return [-1, -1, -1]

    def get_hsv_hue(self, idx: int) -> int:
        """Returns the hue of the HSV color for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            int: The hue (0 - 360)
        """
        return self.get_hsv(idx)[0]

    def get_hsv_saturation(self, idx: int) -> int:
        """Returns the saturation of the HSV color for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            int: The saturation (0 - 100)
        """
        return self.get_hsv(idx)[1]

    def get_hsv_value(self, idx: int) -> int:
        """Returns the brightness (value) of the HSV color for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            int: The brightness (0 - 100)
        """
        return self.get_hsv(idx)[2]

    def get_hsv(self, idx: int) -> List[int]:
        """Returns the HSV color for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            List[int]: The HSV color
        """
        result = self.__read_color(idx)
        if result is not None:
            white_value = 256 * result[8] + result[7]
            h, s, v = colorsys.rgb_to_hsv(
                (256 * result[2] + result[1]) / white_value,
                (256 * result[4] + result[3]) / white_value,
                (256 * result[6] + result[5]) / white_value
            )
            return [int(h * 360), int(s * 100), int(v * 100)]
        return [-1, -1, -1]

    def get_hex(self, idx: int) -> str:
        """Returns the HEX color for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            str: The HEX color
        """
        hsv = self.get_hsv(idx)
        r, g, b = colorsys.hsv_to_rgb(hsv[0] / 360, hsv[1] / 100, hsv[2] / 100)
        return "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))

    def get_white_value(self, idx: int) -> int:
        """Returns the white value for a specific sensor.

        Args:
            idx (int): The sensor index (0-7)

        Returns:
            int: The ambient light (0 - 65535)
        """
        result = self.__read_color(idx)
        if result is not None:
            return 256 * result[8] + result[7]
        return -1

    def __init_sensor(self, idx: int, mt = 2, led_1_pwm = 0, led_2_pwm = 0, led_3_pwm = 0):
        """Initialize measurement time and brightness of all LEDs for a specific sensor.

        The measurement time constants:
        - 0 = 40ms
        - 1 = 80ms
        - 2 = 160ms (default)
        - 3 = 320ms
        - 4 = 640ms
        - 5 = 1280ms

        Args:
            idx (int): The sensor index (0-7)
            mt (int, optional): The measurement time. Defaults to 2.
            led_1_pwm (int, optional): The brightness of the first LED. Defaults to 0.
            led_2_pwm (int, optional): The brightness of the second LED. Defaults to 0.
            led_3_pwm (int, optional): The brightness of the third LED. Defaults to 0.

        Raises:
            ValueError: If the measurement time is less than 0 or greater than 5
        """
        if mt not in [0,1,2,3,4,5]:
            raise ValueError("The measurement time must be >= 0 and <=5")

        self.__i2c.write_i2c_block_data(ADDRESS.RGB, (REGISTER.INIT_SENSOR_X + idx) & 0xff,  [mt & 0xff, led_1_pwm & 0xff, led_2_pwm & 0xff, led_3_pwm & 0xff])
        self.__mtx[idx] = mt
        self.__pwm[idx] = [led_1_pwm, led_2_pwm, led_3_pwm]

    def __read_color(self, idx: int):
        result = self.__i2c.read_i2c_block_data(ADDRESS.RGB, REGISTER.GET_COLOR_X + idx, 11)
        if len(result) == 11:
            return result
        return None

    def __sensor_test(self):
        """Self-test of the I2C addresses.
        Raises:
            RuntimeError: If the sensor cannot be read.
        """
        try:
            self.__i2c.read_i2c_block_data(ADDRESS.RGB, REGISTER.FW_VERSION, 2)
        except IOError:
            raise RuntimeError("Unable to identify RGB sensor chip at 0x{:02x} (IOError)".format(ADDRESS.RGB))

    def __up_range(self, start: int, stop: int, step: int):
        while start <= stop:
            yield start
            start += abs(step)

    def __down_range(self, start: int, stop: int, step: int):
        while start >= stop:
            yield start
            start -= abs(step)
