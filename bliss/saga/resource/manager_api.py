# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

__author__    = "Ole Christian Weidner"
__copyright__ = "Copyright 2012, Ole Christian Weidner"
__license__   = "MIT"

import bliss.saga 
from bliss.saga import Url
from bliss.saga.object_api import Object 

class Manager(Object):

    ######################################################################
    ## 
    def __init__(self, url, session=None):
        '''Construct a new resource manager object
           @param url: Url of the (remote) resource manager.
           @type  url: L{Url} 
        '''
        Object.__init__(self, Object.Type.ResourceManager, 
                        apitype=Object.Type.ResourceAPI, session=session)

        if(type(url) == str):
            self._url = Url(str(url))
        else:
            self._url = url

        self._plugin = Object._get_plugin(self) # throws 'NoSuccess' on error
        self._plugin.register_manager_object(self, url)
        self._logger.info("Bound to plugin %s" % (repr(self._plugin)))

    ######################################################################
    ## 
    def __del__(self):
        '''Delete the manager in a civilised fashion.'''
        if self._plugin is not None:
            self._plugin.unregister_manager_object(self)
        else:
            pass # can't throw here

    ######################################################################
    ## 
    def list_compute_resources(self):
        '''List known compute resource ids'''
        if self._plugin is None:
            raise bliss.saga.Exception(bliss.saga.Error.NoSuccess, 
              "Object not bound to a plugin")

        return self._plugin.manager_list_compute_resources(self)

    ######################################################################
    ## 
    def list_storage_resources(self):
        '''List known resource storage ids'''
        if self._plugin is None:
            raise bliss.saga.Exception(bliss.saga.Error.NoSuccess, 
              "Object not bound to a plugin")

        return self._plugin.manager_list_storage_resources(self)

    ######################################################################
    ## 
    def list_compute_templates(self):
        '''List available template names'''
        if self._plugin is None:
            raise bliss.saga.Exception(bliss.saga.Error.NoSuccess, 
              "Object not bound to a plugin")

        return self._plugin.manager_list_compute_templates(self)

    ######################################################################
    ## 
    def list_storage_templates(self):
        '''List available template names'''
        if self._plugin is None:
            raise bliss.saga.Exception(bliss.saga.Error.NoSuccess, 
              "Object not bound to a plugin")

        return self._plugin.manager_list_storage_templates(self)

    ######################################################################
    ## 
    def get_template_details(self, t_id):
        '''get template description'''
        if self._plugin is None:
            raise bliss.saga.Exception(bliss.saga.Error.NoSuccess, 
              "Object not bound to a plugin")

        return self._plugin.manager_get_template_details(self, t_id)


    ######################################################################
    ## 
    def create_compute(self, compute_description):
        '''Instantiate (request) a new compute resource'''

        if compute_description.get_type() != Object.Type.ResourceComputeDescription:
            raise bliss.saga.Exception(bliss.saga.Error.BadParameter, 
                  "create_compute() expects %s object as parameter" 
                  % (Object.Type.ResourceComputeDescription))

        if self._plugin is None:
            raise bliss.saga.Exception(bliss.saga.Error.NoSuccess, 
              "Object not bound to a plugin")

        return self._plugin.manager_create_compute(self, compute_description)


    ######################################################################
    ## 
    def get_compute(self, compute_id):
        '''Return the resource handle for an existing compute resource'''
        if self._plugin is None:
            raise bliss.saga.Exception(bliss.saga.Error.NoSuccess, 
              "Object not bound to a plugin")

        return self._plugin.manager_get_compute(self, compute_id)


    ######################################################################
    ## 
    def destroy_compute(self, compute_id, drain=False):
        '''Destroy (close) an existing compute resource'''
        if self._plugin is None:
            raise bliss.saga.Exception(bliss.saga.Error.NoSuccess, 
              "Object not bound to a plugin")

        return self._plugin.manager_destroy_compute(self, compute_id, drain)


    ######################################################################
    ## 
    def create_storage(self, storage_description):
        '''Instantiate (request) a new storage resource'''

        if storage_description.get_type() != Object.Type.ResourceStorageDescription:
            raise bliss.saga.Exception(bliss.saga.Error.BadParameter, 
                  "create_storage() expects %s object as parameter" 
                  % (Object.Type.ResourceStorageDescription))

        if self._plugin is None:
            raise bliss.saga.Exception(bliss.saga.Error.NoSuccess, 
              "Object not bound to a plugin")

        return self._plugin.manager_create_storage(self, storage_description)


    ######################################################################
    ## 
    def get_storage(self, storage_id):
        '''Return the resource handle for an existing storage resource'''
        if self._plugin is None:
            raise bliss.saga.Exception(bliss.saga.Error.NoSuccess, 
              "Object not bound to a plugin")

        return self._plugin.manager_get_storage(self, storage_id)


    ######################################################################
    ## 
    def destroy_storage(self, storage_id, drain=False):
        '''Destroy (close) an existing storage resource'''
        if self._plugin is None:
            raise bliss.saga.Exception(bliss.saga.Error.NoSuccess, 
              "Object not bound to a plugin")

        return self._plugin.manager_destroy_storage(self, storage_id, drain)


