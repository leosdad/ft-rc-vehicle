#!/usr/bin/python
# -*- coding: UTF-8 -*-
from .Txt4Encodermotor import Txt4Encodermotor
from .Txt4Motor import Txt4Motor
from ..MotorFactory import MotorFactory


class Txt4MotorFactory(MotorFactory):

    def create_motor(self, controller, identifier):
        """Create a Txt4 motor.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: Txt4Motor
        """
        return Txt4Motor(controller, identifier)

    def create_encodermotor(self, controller, identifier):
        """Create a Txt4 encoder motor.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: Txt4Encodermotor
        """
        return Txt4Encodermotor(controller, identifier)
