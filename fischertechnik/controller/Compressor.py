#!/usr/bin/python
# -*- coding: UTF-8 -*-

from .Output import Output


class Compressor(Output):

    def __init__(self, controller, identifier):
        """@ParamType controller fischertechnik.controller.BaseController
        @ParamType identifier int"""
        Output.__init__(self, controller, identifier)
