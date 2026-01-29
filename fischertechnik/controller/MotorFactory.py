#!/usr/bin/python
# -*- coding: UTF-8 -*-

class MotorFactory(object):
    def __init__(self):
        object.__init__(self)

    def create_motor(self, controller, identifier):
        """Create a motor.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: Motor
        """
        pass

    def create_encodermotor(self, controller, identifier):
        """Create an encoder motor.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: Encodermotor
        """
        pass



