#!/usr/bin/python
# -*- coding: UTF-8 -*-
from .IOUnit import IOUnit

class Output(IOUnit):

    MIN_VALUE = 0
    MAX_VALUE = 512

    """Abstract Output"""
    def __init__(self, controller, identifier):
        """@ParamType controller fischertechnik.controller.BaseController
        @ParamType identifier int"""
        IOUnit.__init__(self, controller, identifier)
        self._controller.set_output(self._identifier, self)

    def __del__(self):
        self.off()

    def on(self):
        """@ParamType brightness int
        @ReturnType void"""
        pass

    def off(self):
        """@ReturnType int"""
        pass

    def is_on(self):
        """@ReturnType boolean"""
        pass

    def is_off(self):
        """@ReturnType boolean"""
        pass

    def validate_value(self, value):
        if value < self.MIN_VALUE or value > self.MAX_VALUE:
            raise ValueError("Value must be >0 and <=512")
