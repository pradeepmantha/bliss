# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

__author__    = "Ole Christian Weidner"
__copyright__ = "Copyright 2012, Ole Christian Weidner"
__license__   = "MIT"

from bliss.saga import Url
from bliss.saga.Object import Object 

class Compute(Object):

    ######################################################################
    ## 
    def __init__(self):
        '''PRIVATE: Create a new compute resource.
        '''
        Object.__init__(self, Object.Type.ResourceCompute, 
                        apitype=Object.Type.ResourceAPI)


    ######################################################################
    ##
    #  FIXME: not sure if that should be overloaded or not...
    def __init_from_manager(self, manager_obj, compute_description):
        '''(Hidden) Constructor'''
        self._manager = manager_obj
        self._url     = manager_obj._url
        self._compute_description = compute_description

        self._plugin  = Object._get_plugin(self) # throws 'NoSuccess' on error
        self._logger.info("Bound to plugin %s" % (repr(self._plugin)))

    ######################################################################
    ##
    def get_state(self):
        '''Return the state of the resource'''
        if self._plugin is None:
            raise bliss.saga.Exception(bliss.saga.Error.NoSuccess, 
                                       "Object not bound to a plugin")
        
        return self._plugin.compute_resource_get_state(self)
    
    
    ######################################################################
    ##
    def get_state_detail(self):
        '''Return the state detail of the resource'''
        if self._plugin is None:
            raise bliss.saga.Exception(bliss.saga.Error.NoSuccess, 
                                       "Object not bound to a plugin")
        
        return self._plugin.compute_resource_get_state_detail(self)
    
    
    ######################################################################
    ##
    def get_id(self):
        '''Return the id of the resource'''
        if self._plugin is None:
            raise bliss.saga.Exception(bliss.saga.Error.NoSuccess, 
                                       "Object not bound to a plugin")
        
        return self._plugin.compute_resource_get_id(self)
    
    
    ######################################################################
    ##
    def get_manager(self):
        '''Return the associated resource manager object.'''
        if self._plugin is None:
            raise bliss.saga.Exception(bliss.saga.Error.NoSuccess, 
                                       "Object not bound to a plugin")
        
        return self._plugin.compute_resource_get_manager(self)
    
    
    ######################################################################
    ##
    def get_description(self): 
        '''Return the associated resource description object.'''
        if self._plugin is None:
            raise bliss.saga.Exception(bliss.saga.Error.NoSuccess, 
                                       "Object not bound to a plugin")
        
        return self._plugin.compute_resource_get_description(self)
    
    ######################################################################
    ##
    def destroy(self, drain=False):
        '''Destroy (close) the resource.'''
        if self._plugin is None:
            raise bliss.saga.Exception(bliss.saga.Error.NoSuccess, 
                                       "Object not bound to a plugin")
        
        return self._plugin.compute_resource_destroy(self, drain)
    
    
    ######################################################################
    ##
    def wait(self, timeout=-1, state="Final"):
        '''Wait for the resource to reach a specific state.'''
        if self._plugin is None:
            raise bliss.saga.Exception(bliss.saga.Error.NoSuccess, 
                                       "Object not bound to a plugin")
        
        return self._plugin.compute_resource_wait(self, state)
