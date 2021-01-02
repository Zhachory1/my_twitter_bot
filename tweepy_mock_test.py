import unittest
from tweepy_mock import TweepyMock, UserMock

class TestTweepyMock(unittest.TestCase):

    def test_something(self):
        pass


class TestUserMock(unittest.TestCase):
    def tearDown(self):
        UserMock.reset()

    def test_make_user(self):
        new_user = UserMock()
        self.assertEqual(new_user.name, "User1")
        print(str(new_user))
        self.assertEqual(new_user.followers(), [])

    def test_second_user(self):
        first_user = UserMock()
        second_user = UserMock()
        self.assertEqual(second_user.name, "User2")
        print(str(second_user))
        self.assertEqual(second_user.followers(), [first_user])


if __name__ == '__main__':
    unittest.main()