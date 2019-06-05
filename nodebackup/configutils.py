import os
from os.path import expanduser
from pathlib import Path

def homedirectory():
    return expanduser("~")

def configdirectory():
    return homedirectory() + '/.lncm'

def configfile():
    return configdirectory() + '/nodebackup.toml'

def pathExists(thepath):
    return Path(thepath).exists()

def isDirectory(thepath):
    return (Path(thepath).is_dir() and Path(thepath).exists())

def canAccessForWriting(thepath):
    return os.access(os.path.dirname(os.path.realpath(thepath)), os.W_OK)

if __name__ == "__main__":
    print("This file is not meant to be run directly")