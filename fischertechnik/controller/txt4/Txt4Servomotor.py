#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ..Servomotor import Servomotor


class Txt4Servomotor(Servomotor):

    def __init__(self, controller, identifier):
        """Txt4 servo motor.

        @param controller: BaseController
        @param identifier: int servo index
        """
        self.instance = controller._txt.servo(identifier)
        controller._txt.update_config()
        Servomotor.__init__(self, controller, identifier)

    def set_position(self, position):
        """Set position.

        @param position: int (0-512)
        """
        self.validate_position(position)
        self.instance.pwm_set(position)

    def get_position(self):
        """Get position.

        @return: int
        """
        return self.instance.pwm
