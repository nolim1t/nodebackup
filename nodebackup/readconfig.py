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

import sys
from configutils import configfile, configdirectory, isDirectory, pathExists, canAccessConfigFile

def initconfig():
    import toml

    if not isDirectory(configdirectory()):
        print("Directory .lncm doesn't exist")
        sys.exit(1)

    # Check if config file exists
    if not canAccessConfigFile():
        print("Config file can not be accessed")
        sys.exit(1)


    try:
        return toml.load(configfile(), _dict=dict)
    except:
        exception = sys.exc_info()[0]
        print("Failed to load config (%s)" % exception)
        sys.exit(1)

if __name__ == "__main__":
    print("This file is not meant to be run directly")