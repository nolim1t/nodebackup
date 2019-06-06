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

# Check for logfile
if not 'logfile' in configuration:
    print("no logfile path defined!")
    sys.exit(1)
# Check pidfile
if not 'pidfile' in configuration:
    pidfile = "/var/run/nodebackup.pid"
else:
    pidfile = configuration['pidfile']

# Check backup file
if not 'backupfile' in configuration:
    # Default path
    backupfile = "/media/important/important/lnd/data/chain/bitcoin/mainnet/channel.backup"
else:
    # Define the location of the backup in config
    backupfile = configuration['backupfile']

# Set up logging
logging.basicConfig(filename=configuration['logfile'], level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


# # See <https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/>
# Define dropbox connection
logging.info('Started daemon')
logging.info('Dropbox connection initialized')

# Add handlers
from stophandler import handler_stop_signals
signal.signal(signal.SIGTERM, handler_stop_signals)
signal.signal(signal.SIGHUP, handler_stop_signals)
signal.signal(signal.SIGINT, handler_stop_signals)
signal.signal(signal.SIGQUIT, handler_stop_signals)               

def watch(fileparam):
    # File notify libraries
    import inotify.adapters    
    # Cloud backup libraries
    from cloudutils import dropboxbackup    
    from configutils import canAccessForWriting, pathExists
    
    if pathExists(fileparam):
        i = inotify.adapters.Inotify()
        i.add_watch(fileparam)
        logging.info("Watching file " + fileparam + " for changes")
        for event in i.event_gen(yield_nones=False):
            (_, type_names, path, filename) = event
            logging.debug("File changed with flag: " + str(type_names))
            logged_debug_watch = "Path: %s Filename %s" % (path, filename)
            logging.debug(logged_debug_watch)
            if type_names == ['IN_MODIFY']:
                logging.info('File ' + fileparam + ' Changed.. uploading to defined cloud services')
                dropboxbackup(filename=fileparam)
    else:
        logging.warn("File doesn't exist.. waiting for 10 minutes before checking again")
        time.sleep(600)      

def startdaemon():
    from configutils import canAccessForWriting
    # Forking stuff
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
    
    watch(backupfile)
    
    # End Daemon function

# Main entrypoint
def main():
    startdaemon()

if __name__ == '__main__':
    main()