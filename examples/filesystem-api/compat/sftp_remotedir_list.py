#!/usr/bin/env python

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

'''This examples shows how to copy a file to a remote 
   host via ssh using a custom security context.

   If something doesn't work as expected, try to set 
   SAGA_VERBOSE=3 in your environment before you run the
   script in order to get some debug output.

   If you think you have encountered a defect, please 
   report it at: https://github.com/oweidner/bliss/issues
'''

__author__    = "Ole Christian Weidner"
__copyright__ = "Copyright 2011, Ole Christian Weidner"
__license__   = "MIT"

import time
import bliss.sagacompat as saga

def main():
    
    try:
        # set up a security context (optional)
        # if no security context is defined, the PBS
        # plugin will pick up the default set of ssh 
        # credentials of the user, i.e., ~/.ssh/id_rsa
        ctx = saga.context()
        ctx.type = saga.context.SSH
        ctx.userid  = 'oweidner' # like 'ssh username@host ...'
        ctx.userkey = '/Users/s1063117/.ssh/id_rsa' # like ssh -i ...'

        session = saga.session()
        session.contexts.append(ctx)
 
        mydir = saga.filesystem.directory("sftp://india.futuregrid.org/tmp", session=session)
        for entry in mydir.list():
            print entry

    except saga.exception, ex:
        print "Oh, snap! An error occured: %s" % (str(ex))

if __name__ == "__main__":
    main()
