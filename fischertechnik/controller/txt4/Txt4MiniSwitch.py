#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ..MiniSwitch import MiniSwitch


class Txt4MiniSwitch(MiniSwitch):

    instance = None

    def __init__(self, controller, identifier):
        """Txt4 mini switch.

        @param controller: BaseController
        @param identifier: int input index
        """
        self.instance = controller._txt.switch(identifier)
        controller._txt.update_config()
        MiniSwitch.__init__(self, controller, identifier)

    def get_state(self):
        """Get switch state.

        @return: int
        """
        return self.instance.state()

    def is_open(self):
        """Return True if switch is open.

        @return: bool
        """
        return self.get_state() == 0

    def is_closed(self):
        """Return True if switch is closed.

        @return: bool
        """
        return self.get_state() == 1
