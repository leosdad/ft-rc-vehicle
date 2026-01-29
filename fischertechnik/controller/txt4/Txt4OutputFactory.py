#!/usr/bin/python
# -*- coding: UTF-8 -*-
from .Txt4Compressor import Txt4Compressor
from .Txt4LightSource import Txt4LightSource
from .Txt4MagneticValve import Txt4MagneticValve
from .Txt4UnidirectionalMotor import Txt4UnidirectionalMotor
from ..OutputFactory import OutputFactory


class Txt4OutputFactory(OutputFactory):

    def create_lamp(self, controller, identifier):
        """Create a Txt4 lamp/light output.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: Txt4LightSource
        """
        return Txt4LightSource(controller, identifier)

    def create_led(self, controller, identifier):
        """Create a Txt4 LED output.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: Txt4LightSource
        """
        return Txt4LightSource(controller, identifier)

    def create_magnetic_valve(self, controller, identifier):
        """Create a Txt4 magnetic valve output.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: Txt4MagneticValve
        """
        return Txt4MagneticValve(controller, identifier)

    def create_compressor(self, controller, identifier):
        """Create a Txt4 compressor output.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: Txt4Compressor
        """
        return Txt4Compressor(controller, identifier)

    def create_unidirectional_motor(self, controller, identifier):
        """Create a Txt4 unidirectional motor output.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: Txt4UnidirectionalMotor
        """
        return Txt4UnidirectionalMotor(controller, identifier)