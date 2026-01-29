#!/usr/bin/python
# -*- coding: UTF-8 -*-
from .IOUnit import IOUnit

class Output(IOUnit):

    MIN_VALUE = 0
    MAX_VALUE = 512

    """Abstract Output"""
    def __init__(self, controller, identifier):
        """Output base class.

        @param controller: BaseController
        @param identifier: int output index
        """
        IOUnit.__init__(self, controller, identifier)
        self._controller.set_output(self._identifier, self)

    def __del__(self):
        self.off()

    def on(self):
        """Turn output on."""
        pass

    def off(self):
        """Turn output off."""
        pass

    def is_on(self):
        """Return True if output is on.

        @return: bool
        """
        pass

    def is_off(self):
        """Return True if output is off.

        @return: bool
        """
        pass

    def validate_value(self, value):
        if value < self.MIN_VALUE or value > self.MAX_VALUE:
            raise ValueError("Value must be >0 and <=512")
