import unittest

class TestDaemon(unittest.TestCase):
    def setUp(self):
        print("Setup")
        # set up stub config

    def tearDown(self):
        # Remove stub config
         print("Teardown")

    def test_can_daemon_start(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()