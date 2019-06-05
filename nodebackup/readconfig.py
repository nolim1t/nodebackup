import sys
from configutils import configfile, configdirectory, isDirectory, pathExists

def initconfig():
    import toml

    if not isDirectory(configdirectory()):
        print("Directory .lncm doesn't exist")
        sys.exit()
    else:
        print("Directory .lncm exists")

    # Check if config file exists
    if not pathExists(configfile()):
        print("Config file does not exist")
        sys.exit()
    else:
        print("Checking config")

    try:
        return toml.load(configfile(), _dict=dict)
    except:
        exception = sys.exc_info()[0]
        print("Failed to load config (%s)" % exception)
        sys.exit(1)

if __name__ == "__main__":
    print("This file is not meant to be run directly")