#!/usr/bin/env python

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

__author__    = "Ole Christian Weidner"
__email__     = "ole.weidner@me.com"
__copyright__ = "Copyright 2011, Ole Christian Weidner"
__license__   = "MIT"

_api_type_saga_job = "saga.job"
_api_type_saga_file = "saga.file"

import logging
from bliss.plugins import utils
from bliss.saga.exception import Exception as SAGAException

class _PluginBase:
    '''Abstract base class for all plugins'''
    
    def __init__(self, name, schemas):
        '''Class constructor'''
        self.name = name
        self.schemas = schemas
        self.__logger = logging.getLogger(self.__class__.__name__+'('+str(hex(id(self)))+')')

    def get_logger(self):
        '''Return the logger object'''
        return self.__logger

    def log_error_and_raise(self, error, message):
        '''Writes an ERROR to the plugin log and raises an exception'''
        msg = "[%s] %s %s" % (self.name, message, utils.get_traceback())
        self.__logger.error(message)
        raise SAGAException(error, msg)

    def log_info(self, message):
        '''Writes an INFO to the plugin log'''
        self.__logger.info(message)
    
    def log_warning(self, message):
        '''Writes a WARNING to the plugin log'''
        self.__logger.warning(message)


    def log_error(self, message):
        '''Writes an ERROR to the plugin log'''
        self.__logger.error(message)
 
 
    @classmethod
    def supported_api(self):
        '''Return the api package this plugin supports'''
        raise Exception("Requires implementation!")
       

    @classmethod
    def supported_schemas(self):
        '''Implements interface from _PluginBase'''
        return self._schemas

    @classmethod
    def plugin_name(self):
        '''Implements interface from _PluginBase'''
        return self._name

    @classmethod
    def sanity_check(self):
        '''Called upon registring. If an excpetion is thrown, plugin will be disabled.'''
        raise Exception("Requires implementation!")

    def get_runtime_info(self):
        '''This method is used to reveal some runtime information for this plugin'''
  #      raise exception.Exception(exception.Error.NotImplemented, "%s: get_runtime_info() is not supported by this plugin".format(repr(self))) 

