#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ..LightSource import LightSource


class Txt4LightSource(LightSource):
    instance = None

    def __init__(self, controller, identifier):
        """Txt4 light source.

        @param controller: BaseController
        @param identifier: int output index
        """
        self.instance = controller._txt.output(identifier)
        controller._txt.update_config()
        LightSource.__init__(self, controller, identifier)

    def on(self):
        """Turn on (full brightness)."""
        self.instance.setLevel(512)

    def off(self):
        """Turn off."""
        self.instance.setLevel(0)

    def is_on(self):
        """Return True if on.

        @return: bool
        """
        return self.instance.pwm != 0

    def is_off(self):
        """Return True if off.

        @return: bool
        """
        return self.instance.pwm == 0

    def set_brightness(self, brightness):
        """Set brightness.

        @param brightness: int (0-512)
        """
        self.validate_value(brightness)
        self.instance.setLevel(brightness)

    def get_brightness(self):
        """Get brightness.

        @return: int
        """
        return self.instance.pwm
