#!/usr/bin/env python3

"""
Usage: lndnodebackup start
"""

import os, sys, logging
from docopt import docopt

# Internal
import nodebackup.lndbackupdaemon
import nodebackup.configutils

# Check for logfile (Used for general logging. This needs to be in entrypoint)
configuration = nodebackup.configutils.readconfig()
if not 'logfile' in configuration:
    print("no logfile path defined!")
    sys.exit(1)
logging.basicConfig(filename=configuration['logfile'], level=logging.DEBUG, format='%(asctime)s [%(levelname)s]: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


# Main entrypoint
def main():
    args = docopt(__doc__, version="v0.0.2")
    if args["start"]:
        nodebackup.lndbackupdaemon.startdaemon()

if __name__ == '__main__':
    main()