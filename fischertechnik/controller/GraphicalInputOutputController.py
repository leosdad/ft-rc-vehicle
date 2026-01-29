#!/usr/bin/python
# -*- coding: UTF-8 -*-
from .InputOutputController import InputOutputController

class GraphicalInputOutputController(InputOutputController):
    def __init__(self):
        self._ir = None
        # @AssociationType fischertechnik.controller.IR
        # @AssociationMultiplicity 1
        self._gui = None
        # @AssociationType fischertechnik.controller.Window
        # @AssociationMultiplicity 1
        self._usb = []
        # @AssociationType fischertechnik.controller.USB[]
        # @AssociationMultiplicity *
        self._loudspeaker = None
        # @AssociationType fischertechnik.controller.Loudspeaker
        # @AssociationMultiplicity 1
        self._mic = None
        # @AssociationType fischertechnik.controller.Microphone
        # @AssociationMultiplicity 1
        InputOutputController.__init__(self)

    def set_window(self, window):
        """Attach a window (GUI) to the controller.

        @param window: Window
        """
        pass

    def exec_controller(self):
        pass

    def set_usb(self, idx, usb):
        """Set USB device at index.

        @param idx: int (1-based)
        @param usb: USB
        """
        self._usb[idx - 1] = usb

    def get_usb(self, idx):
        """Get USB device at index.

        @param idx: int (1-based)
        @return: USB
        """
        return self._usb[idx - 1]

    def set_loudspeaker(self, loudspeaker):
        """Set loudspeaker.

        @param loudspeaker: Loudspeaker
        """
        self._loudspeaker = loudspeaker

    def get_loudspeaker(self):
        """Get loudspeaker.

        @return: Loudspeaker
        """
        return  self._loudspeaker

    def get_microphone(self):
        """Get microphone.

        @return: Microphone
        """
        pass

    def get_ir(self):
        """Get IR interface.

        @return: IR
        """
        pass

