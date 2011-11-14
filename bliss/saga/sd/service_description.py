#!/usr/bin/env python

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

__author__    = "Ole Christian Weidner"
__email__     = "ole.weidner@me.com"
__copyright__ = "Copyright 2011, Ole Christian Weidner"
__license__   = "MIT"

from bliss.saga.object import Object
from bliss.saga.attributes import AttributeInterface
from bliss.saga.url import Url

class ServiceDescription(Object, AttributeInterface):
    '''Loosely represents a SAGA service description as defined in GFD-R-P.114'''

    def __init__(self):
        '''Constructor.'''
        Object.__init__(self, Object.JobDescription, 
                        apitype=Object.JobAPI,)
        AttributeInterface.__init__(self)

        self._url         = None
        self._type        = None
        self._uid         = None
        self._site        = None
        self._name        = None
        self._implementor = None

        # register properties with the attribute interface
        self._register_ro_attribute     (name="URL", 
                                         accessor=self.__class__.url) 
        self._register_ro_attribute     (name="UID", 
                                         accessor=self.__class__.uid) 
        self._register_ro_attribute     (name="Type", 
                                         accessor=self.__class__.type) 
        self._register_ro_attribute     (name="Site", 
                                         accessor=self.__class__.site) 
        self._register_ro_attribute     (name="Name", 
                                         accessor=self.__class__.name) 
        self._register_ro_attribute     (name="Implementor", 
                                         accessor=self.__class__.implementor) 

    def __del__(self):
        '''Destructor'''
        pass

    def get_data():
        '''Return the service data object.'''
        pass

    ######################################################################
    ## Property
    def url():
        doc = "The URL to contact the serivce."
        def fget(self):
            return self._url
        return locals()
    url = property(**url())
      
    ######################################################################
    ## Property
    def uid():
        doc = "The unique identifier of the service."
        def fget(self):
            return self._uid
        return locals()
    uid = property(**uid())

    ######################################################################
    ## Property
    def type():
        doc = "The type of the service."
        def fget(self):
            return self._type
        return locals()
    type = property(**type())

    ######################################################################
    ## Property
    def site():
        doc = "Name of the site of the service."
        def fget(self):
            return self._site
        return locals()
    site = property(**site())

    ######################################################################
    ## Property
    def name():
        doc = "(Descriptive) name of the service."
        def fget(self):
            return self._name
        return locals()
    name = property(**name())

    ######################################################################
    ## Property
    def implementor():
        doc = "Name of the organization providing the implementation of the service."
        def fget(self):
            return self._implementor
        return locals()
    implementor = property(**implementor())
