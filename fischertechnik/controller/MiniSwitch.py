#!/usr/bin/python
# -*- coding: UTF-8 -*-
from .Input import Input

class MiniSwitch(Input):
    def __init__(self, controller, identifier):
        """Mini switch base class.

        @param controller: BaseController
        @param identifier: int input index
        """
        Input.__init__(self, controller, identifier)

    def get_state(self):
        """Get switch state.

        @return: int
        """
        pass

    def is_open(self):
        """Return True if switch is open.

        @return: bool
        """
        pass

    def is_closed(self):
        """Return True if switch is closed.

        @return: bool
        """
        pass

