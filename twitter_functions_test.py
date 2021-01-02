import unittest
from twitter_functions import TwitterInterface

class TestTwitterInterface(unittest.TestCase):
    def setUp(self):
        self.test_api = TwitterInterface("", "", "", "")
        self.test_api.api = TweepyMock()
        self.test_api.authenticated = True

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()