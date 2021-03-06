#!/usr/bin/env python

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

'''This examples shows how to submit a job to the local machine

   If something doesn't work as expected, try to set 
   SAGA_VERBOSE=3 in your environment before you run the
   script in order to get some debug output.

   If you think you have encountered a defect, please 
   report it at: https://github.com/oweidner/bliss/issues
'''

__author__    = "Ole Christian Weidner"
__copyright__ = "Copyright 2012, Ole Christian Weidner"
__license__   = "MIT"

import time
import bliss.saga as saga

def main():
    
    try:
        # create a job service for the local machine
        js = saga.job.Service("fork://localhost")

        # describe our job
        jd = saga.job.Description()
        # resource requirements
        jd.wall_time_limit  = 5 # minutes
        jd.total_cpu_count = 1     
        # environment, executable & arguments
        jd.environment = {'SLEEP_TIME':'10'}       
        jd.executable  = '/bin/sleep'
        jd.arguments   = ['$SLEEP_TIME']
        # output options
        jd.output = "bliss_pbssh_job.stdout"
        jd.error  = "bliss_pbssh_job.stderr"

        # create the job (state: New)
        myjob = js.create_job(jd)

        print "Job ID    : %s" % (myjob.jobid)
        print "Job State : %s" % (myjob.get_state())

        print "\n...starting job...\n"
        # run the job (submit the job to PBS)
        myjob.run()

        print "Job ID    : %s" % (myjob.jobid)
        print "Job State : %s" % (myjob.get_state())

        print "\n...waiting for job...\n"
        # wait for the job to either finish or fail
        myjob.wait()

        print "Job State : %s" % (myjob.get_state())
        print "Exitcode  : %s" % (myjob.exitcode)

    except saga.Exception, ex:
        print "Oh, snap! An error occured: %s" % (str(ex))

if __name__ == "__main__":
    main()

# INFO: The PBS script generated behind the scenes by the  
#       plugin looks like this (SAGA_VERBOSE=6 shows it):
#       
#         #!/bin/bash 
#         #PBS -N bliss_job 
#         #PBS -V     
#         #PBS -o bliss_pbssh_job.stdout 
#         #PBS -e bliss_pbssh_job.stderr 
#         #PBS -l walltime=0:05:00 
#         #PBS -v SLEEP_TIME=10, 
#       
#         /bin/sleep $SLEEP_TIME 

