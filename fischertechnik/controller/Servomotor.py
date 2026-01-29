#!/usr/bin/python
# -*- coding: UTF-8 -*-
from .IOUnit import IOUnit

class Servomotor(IOUnit):

    MIN_POSITION = 0
    MAX_POSITION = 512

    def __init__(self, controller, identifier):
        """Servomotor base class.

        @param controller: BaseController
        @param identifier: int servo index
        """
        IOUnit.__init__(self, controller, identifier)
        self._controller.set_servomotor(self._identifier, self)

    def set_position(self, position):
        """Set servo position.

        @param position: int (0-512)
        """
        pass

    def get_position(self):
        """Get servo position.

        @return: int
        """
        pass

    def validate_position(self, position):
        if position < self.MIN_POSITION or position > self.MAX_POSITION:
            raise ValueError("Position must be >0 and <=512")

