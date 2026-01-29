#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ..events.EventLoop import EventLoop

class IOUnit(object):

    _event_loop = None

    def __init__(self, controller, identifier):
        """Base class for IO units.

        @param controller: BaseController
        @param identifier: int
        """
        self._controller = controller
        """@AttributeType fischertechnik.controller.BaseController"""
        self._identifier = identifier
        """@AttributeType int"""
        self._event_loop = EventLoop.getInstance()
        """@AttributeType fischertechnik.events.EventLoop"""
    
    def add_change_listener(self, property_name, callback):
        """Add a property change listener.

        @param property_name: str
        @param callback: callable
        """
        self._event_loop.add_change_listener(self, property_name, callback)
        
    def remove_change_listener(self, property_name, callback):
        """Remove a property change listener.

        @param property_name: str
        @param callback: callable
        """
        self._event_loop.remove_change_listener(self, property_name, callback)
