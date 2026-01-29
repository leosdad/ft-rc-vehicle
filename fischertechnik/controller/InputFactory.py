#!/usr/bin/python
# -*- coding: UTF-8 -*-

class InputFactory(object):
    def __init__(self):
        object.__init__(self)

    def create_ntc_resistor(self, controller, identifier):
        """Create an NTC resistor input.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: NTCResistor
        """
        pass

    def create_photo_resistor(self, controller, identifier):
        """Create a photo resistor input.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: Resistor
        """
        pass

    def create_ultrasonic_distance_meter(self, controller, identifier):
        """Create an ultrasonic distance meter input.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: UltrasonicDistanceMeter
        """
        pass

    def create_photo_transistor(self, controller, identifier):
        """Create a photo transistor input.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: PhotoTransistor
        """
        pass

    def create_color_sensor(self, controller, identifier):
        """Create a color sensor input.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: ColorSensor
        """
        pass

    def create_trail_follower(self, controller, identifier):
        """Create a trail follower input.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: TrailFollower
        """
        pass

    def create_mini_switch(self, controller, identifier):
        """Create a mini switch input.

        @param controller: GraphicalInputOutputController
        @param identifier: int
        @return: MiniSwitch
        """
        pass

