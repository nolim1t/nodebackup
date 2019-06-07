import unittest
from sys import path
path.append("..")
from nodebackup.nodebackup import configutils

from os.path import expanduser

class TestConfigUtils(unittest.TestCase):
    def test_homedir(self):
        self.assertEqual(configutils.homedirectory(), expanduser("~"))
    def test_configdir(self):
        self.assertEqual(configutils.configdirectory(), expanduser("~") + "/.lncm")
    def test_pathexists(self):
        self.assertTrue(configutils.pathExists(expanduser("~")))
    def test_readconfig(self):
        self.assertTrue(configutils.readconfig())

if __name__ == '__main__':
    unittest.main()