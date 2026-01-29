#!/usr/bin/python
# -*- coding: UTF-8 -*-
from .Txt4Servomotor import Txt4Servomotor
from ..ServomotorFactory import ServomotorFactory


class Txt4ServomotorFactory(ServomotorFactory):

    def create_servomotor(self, controller, identifier):
        """Create a Txt4 servo motor.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: Txt4Servomotor
        """
        return Txt4Servomotor(controller, identifier)
