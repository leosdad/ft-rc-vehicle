#!/usr/bin/python
# -*- coding: UTF-8 -*-
from .IOUnit import IOUnit

class Motor(IOUnit):

    # CCW = positive values, direction of rotation is left (0 to +512)
    # CW = negative values, direction of rotation is right (0 to -512)
    # These value ranges correspond to the old ROBOPro.
    CCW = 1
    CW = -1
    MIN_SPEED = -512
    MAX_SPEED = 512

    def __init__(self, controller, identifier):
        """Motor base class.

        @param controller: BaseController
        @param identifier: int motor index
        """
        IOUnit.__init__(self, controller, identifier)
        self._controller.set_motor(self._identifier, self)

    def __del__(self):
        self.stop()

    def set_speed(self, speed, direction):
        """Set motor speed.

        @param speed: int (0-512)
        @param direction: int (Motor.CW or Motor.CCW)
        """
        pass

    def get_speed(self):
        """Get current speed.

        @return: int
        """
        pass

    def is_running(self):
        """Return True if motor is running.

        @return: bool
        """
        pass

    def start(self):
        """Start motor."""
        pass

    def stop(self):
        """Stop motor."""
        pass

    def coast(self):
        """Coast motor."""
        pass

    def validate_speed(self, speed):
        if speed < self.MIN_SPEED or speed > self.MAX_SPEED:
            raise ValueError("Speed must be >=-512 and <=512")