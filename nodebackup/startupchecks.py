from nodebackup.configutils import configfile, configdirectory, isDirectory, pathExists, canAccessForWriting

def checkConfigDirectory():
    if not isDirectory(configdirectory()):
        return False
    else:
        return True
    
if __name__ == "__main__":
    print("This file is not meant to be run directly")