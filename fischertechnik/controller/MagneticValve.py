#!/usr/bin/python
# -*- coding: UTF-8 -*-
from .Output import Output

class MagneticValve(Output):
    def __init__(self, controller, identifier):
        """Magnetic valve base class.

        @param controller: BaseController
        @param identifier: int output index
        """
        Output.__init__(self, controller, identifier)
