#!/usr/bin/env python

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

__author__    = "Ole Christian Weidner"
__email__     = "ole.weidner@me.com"
__copyright__ = "Copyright 2011, Ole Christian Weidner"
__license__   = "MIT"

import bliss.saga

from bliss.saga.object import Object 
from bliss.saga import exception
from bliss.saga.url import Url

class Service(Object):
    '''Loosely represents a SAGA job service as defined in GFD.90'''
    def __init__(self, url, session=None):
        '''Construct a new job service object
           @param url: Url of the (remote) job manager.
           @type  url: L{Url} 
        '''
        if(type(url) == str):
            self._url = Url(str(url))
        else:
            # assume it's a URL object
            self._url = url

        Object.__init__(self, Object.JobService, 
                            apitype=Object.JobAPI, session=session)
        self._plugin = Object._get_plugin(self) # throws 'NoSuccess' on error
        self._plugin.register_service_object(self)
        self._logger.info("Bound to plugin %s" % (repr(self._plugin)))

    def __del__(self):
        '''Destructor.
        '''
        if self._plugin is not None:
            self._plugin.unregister_service_object(self)

    ######################################################################
    ##
    def create_job(self, job_description):
        '''Create a new job object.
           @param job_description: The description for the new job.
           @type  job_description: L{Description} 
        '''
        if self._plugin is None:
            raise exception.Exception(exception.Error.NoSuccess, 
              "Object not bound to a plugin")
        else:
            if job_description.get_type() != Object.JobDescription:
                raise exception.Exception(exception.Error.BadParameter, 
                  "create_job() expects "+Object.type_saga_job_description)

            return self._plugin.service_create_job(self, job_description)


    ######################################################################
    ##
    def get_job(self, job_id):
        '''Return the job object for the given job id.
           @param job_id: The job id.
        '''
        if self._plugin is None:
            raise exception.Exception(exception.Error.NoSuccess, 
              "Object not bound to a plugin")
        else:
            return self._plugin.service_get_job(self, job_id)


    ######################################################################
    ##
    def list(self):
        '''List all jobs managed by this service instance.
        '''
        if self._plugin is not None:
            return self._plugin.service_list(self)
        else:
            raise exception.Exception(exception.Error.NoSuccess, "Object not bound to a plugin")


