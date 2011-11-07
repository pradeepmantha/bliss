#!/usr/bin/env python

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

__author__    = "Ole Christian Weidner"
__email__     = "ole.weidner@me.com"
__copyright__ = "Copyright 2011, Ole Christian Weidner"
__license__   = "MIT"

import os
import logging
import bliss.plugins.registry

class Runtime():
    '''Implements the Bliss runtime system'''
    def __init__(self):
        '''Constructs a runtime object'''

        #BLISS_VERBOSE = int(os.getenv('BLISS_VERBOSE'))
        try: 
            SAGA_VERBOSE = int(os.getenv('SAGA_VERBOSE'))
        except Exception:
            SAGA_VERBOSE = 0

        # 4 = DEBUG + INFO + WARNING + ERROR
        if SAGA_VERBOSE >= 4:
            self.loglevel = logging.DEBUG
        # 3 = INFO + WARNING + ERROR
        elif SAGA_VERBOSE == 3:
            self.loglevel = logging.INFO
        # 2 = WARNING + ERROR 
        elif SAGA_VERBOSE == 2:
            self.loglevel = logging.WARNING
        # 1 = ERROR ONLY
        elif SAGA_VERBOSE <= 1:
            self.loglevel = logging.ERROR
  
        logging.basicConfig(level=self.loglevel, datefmt='%m/%d/%Y %I:%M:%S %p',
                    	    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        address=str(hex(id(self)))
        self.logger = logging.getLogger(self.__class__.__name__+'('+address+')') 
        self.logger.info("BLISS runtime instance created at %s" % address)
        self.plugin_class_list = {}
        self.plugin_instance_list = {}
        
        #iterate thrugh plugin registry
        for plugin in bliss.plugins.registry._registry:
            self.logger.info("Plugin %s found with signature: %s" % (plugin["name"], str(plugin)))
            try:
                # see if the plugin can work properly on this system
                plugin["class"].sanity_check()
                self.logger.info("Plugin %s internal sanity check passed" % (plugin["name"]))
                # passed. add it to the list
                for schema in plugin["schemas"]:
                    self.plugin_class_list[schema] = plugin["class"]
                    self.logger.info("Plugin %s registered as handler for Url schema(s) %s://" % (plugin["name"], schema))


            except Exception, ex:
                self.logger.error("Plugin %s sanity check failed: %s. Disabled." % (plugin["name"], str(ex)))

    def get_plugin_for_url(self, url):
        '''Returns a plugin instance for a given url or throws'''
        # first let's check if there's already a plugin-instance active that can handle this url scheme
        if url.scheme in self.plugin_instance_list:
            self.logger.info("Found an existing plugin instance for url scheme %s://: %s" % (str(url.scheme), self.plugin_instance_list[url.scheme]))
            return self.plugin_instance_list[url.scheme]

        elif url.scheme in self.plugin_class_list:                          
            plugin_obj = self.plugin_class_list[url.scheme](url)            
            self.logger.info("Instantiated a new plugin for url scheme %s://: %s" % (str(url.scheme), repr(plugin_obj)))
            self.plugin_instance_list[url.scheme] = plugin_obj
            return plugin_obj
        else:
            error = ("Couldn't find a plugin for url scheme '%s://'" % (url.scheme))
            self.logger.error(error)
            raise Exception(error)


        

