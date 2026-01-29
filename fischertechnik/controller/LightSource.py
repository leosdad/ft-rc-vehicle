#!/usr/bin/python
# -*- coding: UTF-8 -*-
from .Output import Output

class LightSource(Output):
    def __init__(self, controller, identifier):
        """Light source base class.

        @param controller: BaseController
        @param identifier: int output index
        """
        Output.__init__(self, controller, identifier)

    def set_brightness(self, brightness):
        """Set brightness.

        @param brightness: int (0-512)
        """
        pass

    def get_brightness(self):
        """Get brightness.

        @return: int
        """
        pass
