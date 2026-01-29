#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ..MagneticValve import MagneticValve

class Txt4MagneticValve(MagneticValve):

    state = 0
    instance = None

    def __init__(self, controller, identifier):
        """Txt4 magnetic valve.

        @param controller: BaseController
        @param identifier: int output index
        """
        self.instance = controller._txt.output(identifier)
        controller._txt.update_config()
        MagneticValve.__init__(self, controller, identifier)

    def __del__(self):
        self.off()

    def on(self):
        """Turn on."""
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
