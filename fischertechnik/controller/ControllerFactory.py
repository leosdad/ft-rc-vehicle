#!/usr/bin/python
# -*- coding: UTF-8 -*-

class ControllerFactory(object):
    """Abstract factory to be inherited by a concrete factory per controller.
    E.g. TxtAbstractFactory"""
    def __init__(self):
        object.__init__(self)

    def create_graphical_controller(self, ext=0):
        """Create and return a graphical controller.

        @param ext: int (0=master, >0=extension)
        @return: GraphicalInputOutputController
        """
        pass

    def create_graphical_controller_from_info(self, controller, info):
        """Create a graphical controller instance from controller info.

        @param controller: GraphicalInputOutputController
        @param info: ControllerInfo
        @return: GraphicalInputOutputController
        """
        pass

    def get_controller_info_list(self, controller):
        """Return a list of available controller infos.

        @param controller: GraphicalInputOutputController
        @return: list[ControllerInfo]
        """
        pass

