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
import logging
import sys # System Stuff

from configutils import readconfig
from daemon import  startdaemon

# Check for logfile (Used for general logging. This needs to be in entrypoint)
configuration = readconfig()
if not 'logfile' in configuration:
    print("no logfile path defined!")
    sys.exit(1)

logging.basicConfig(filename=configuration['logfile'], level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


# Main entrypoint
def main():
    startdaemon()

if __name__ == '__main__':
    main()