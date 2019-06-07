import unittest
import os, shutil, pathlib

from sys import path
path.append("..")
from nodebackup.nodebackup import configutils

from os.path import expanduser
from subprocess import call

class TestConfigUtils(unittest.TestCase):        
    def test_homedir(self):
        self.assertEqual(configutils.homedirectory(), expanduser("~"))
    def test_configdir(self):
        self.assertEqual(configutils.configdirectory(), expanduser("~") + "/.lncm")
    def test_pathexists(self):
        self.assertTrue(configutils.pathExists(expanduser("~")))

class TestReadConfig(unittest.TestCase):
    def setUp(self):
        if pathlib.Path(expanduser("~") + "/.lncm/nodebackup.toml").exists():
            call(["/bin/mv", expanduser("~") + "/.lncm/nodebackup.toml", expanduser("~") + "/.lncm/nodebackup.toml.bak"])

        with open(pathlib.Path(expanduser("~") + "/.lncm/nodebackup.toml"), "w") as f:
            f.write('provider = "dropbox"')
            f.write("\n")
            f.write('nodename = "testnode"')
            f.write("\n")
            f.write('backupfile = "./backup.txt"')
            f.write("\n")
            f.write('pidfile = "./pidfile.pid"')
            f.write("\n")
            f.write('logfile = "./logfile.log"')
            f.write("\n\n")
            f.write('[apikeys]')
            f.write("\n")
            f.write('dropbox = "apikey"')
    
    # See if config can be read
    def test_readconfig(self):
        self.assertTrue(configutils.readconfig())

    # If backup file exists, then replace file with backup (cleanup)
    def tearDown(self):
        if pathlib.Path(expanduser("~") + "/.lncm/nodebackup.toml.bak").exists():
            call(["/bin/mv", expanduser("~") + "/.lncm/nodebackup.toml.bak", expanduser("~") + "/.lncm/nodebackup.toml"])


if __name__ == '__main__':
    unittest.main()