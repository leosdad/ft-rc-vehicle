#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ..Motor import Motor


class Txt4Motor(Motor):

    instance = None

    def __init__(self, controller, identifier):
        """Initialize Txt4Motor with controller and identifier.

        @param controller: BaseController-like object.
        @param identifier: motor index.
        """
        self.instance = controller._txt.motor(identifier)
        controller._txt.update_config()
        Motor.__init__(self, controller, identifier)

    def set_speed(self, speed, direction=Motor.CCW):
        """Set motor speed (0-512) with direction after validation.

        @param speed: int (0-512)
        @param direction: int (Motor.CW or Motor.CCW)
        """
        self.validate_speed(speed)
        speed = speed * direction
        self.instance.speed_set(speed)

    def get_speed(self):
        """Return current PWM speed (0-512).

        @return: int
        """
        return self.instance.pwm

    def is_running(self):
        """Return True if motor is running (pwm != 0).

        @return: bool
        """
        return self.instance.pwm != 0

    def start(self):
        """Start motor at current speed."""
        self.instance.start_speed(self.get_speed())

    def stop(self):
        """Stop motor immediately."""
        self.instance.stop()

    def coast(self):
        """Coast motor (allow free spin)."""
        self.instance.coast()
