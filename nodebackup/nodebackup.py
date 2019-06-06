'''
   Copyright 2019 nolim1t.co

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''


# System libraries (TODO: Move as much stuff to its own area)
import os
import time
import logging
import signal # Signal Handling Stuff
import sys # System Stuff

# Configuration for backupfile, logfile and pidfile
from configutils import readconfig
configuration = readconfig()

# Check for logfile (Used for general logging. This needs to be in entrypoint)
if not 'logfile' in configuration:
    print("no logfile path defined!")
    sys.exit(1)

# Check pidfile (used for starting up the daemon. To go with Daemon)
if not 'pidfile' in configuration:
    pidfile = "/var/run/nodebackup.pid"
else:
    pidfile = configuration['pidfile']

# Check backup file (Used for watching. To go with Daemon)
if not 'backupfile' in configuration:
    # Default path
    backupfile = "/media/important/important/lnd/data/chain/bitcoin/mainnet/channel.backup"
else:
    # Define the location of the backup in config
    backupfile = configuration['backupfile']

# Set up logging (To go with entrypoint)
logging.basicConfig(filename=configuration['logfile'], level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


# Add handlers
from stophandler import handler_stop_signals
signal.signal(signal.SIGTERM, handler_stop_signals)
signal.signal(signal.SIGHUP, handler_stop_signals)
signal.signal(signal.SIGINT, handler_stop_signals)
signal.signal(signal.SIGQUIT, handler_stop_signals)               

def startdaemon():
    from configutils import canAccessForWriting
    from inotifyutils import watchFile
    logging.info('Started daemon')    
    
    # Forking stuff To background
    try:
        pid = os.fork()
        if pid > 0:
            logging.info("Running process as PID: %d" % pid)
            print('Running process as PID %d' % pid)
            # Check if writing is possible to the specified pid file
            if canAccessForWriting(pidfile):
                print('Using %s as pidfile' % pidfile)
                logging.info('Using %s as pidfile' % pidfile)
                with open(pidfile, 'w') as pidfilepointer:
                    pidfilepointer.write("%d" % pid)
            else:
                print('Cannot write to %s' % pidfile)
                logging.warn('Cannot write to %s' % pidfile)
            os._exit(0)
    except:
        exception = sys.exc_info()[0]
        logging.fatal("Unable to fork")
        print("Unable to fork (%s)" % exception)
        os._exit(1)

    # Start daemon work
    watchFile(backupfile)
    
    # End Daemon function

# Main entrypoint
def main():
    startdaemon()

if __name__ == '__main__':
    main()