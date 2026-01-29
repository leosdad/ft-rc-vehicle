#!/usr/bin/python
# -*- coding: UTF-8 -*-

class OutputFactory(object):
    def __init__(self):
        object.__init__(self)

    def create_lamp(self, controller, identifier):
        """Create a lamp/light output.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: LightSource
        """
        pass

    def create_led(self, controller, identifier):
        """Create an LED output.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: LightSource
        """
        pass

    def create_magnetic_valve(self, controller, identifier):
        """Create a magnetic valve output.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: MagneticValve
        """
        pass

    def create_compressor(self, controller, identifier):
        """Create a compressor output.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: Compressor
        """
        pass

    def create_unidirectional_motor(self, controller, identifier):
        """Create a unidirectional motor output.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: UnidirectionalMotor
        """
        pass