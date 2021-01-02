
class TweepyMock(object):
    def __init__(self):
        pass

    def verify_credentials(self):
        pass

    def home_timeline(self, count=20):
        pass

    def update_status(self, tweet):
        pass

    def get_user(self, user_name):
        pass

    def create_favorite(self, tweet_id):
        pass

    def search(self, query):
        pass

    def trends_place(self, place=1):
        pass


class UserMock(object):
    _userCount = 1
    _userDict = {}
    def __init__(self):
        self.name = self.getFakeUserName(type(self)._userCount)
        self.description = "I am user " + str(type(self)._userCount) + ". Suck a duck!"
        self.location = "Norway, Somewhere"
        self.id = type(self)._userCount
        type(self)._userDict[self.id] = self
        type(self)._userCount += 1

    def getFakeUserName(self, count):
        return "User" + str(type(self)._userCount)

    def followers(self):
        followers = []
        for i in range(1, self.id):
            followers.append(type(self)._userDict[self.id])
        return followers

    def __str__(self):
        string = ""
        string += "{" + "\n"
        string += self.name + "\n"
        string += self.description + "\n"
        string += "followers: [" + "\n"
        for f in self.followers():
            string += "  " + f.name + "\n"
        string += "]}" + "\n"
        return string

    def __repr__(self):
        return str(self)

    @classmethod
    def reset(cls):
        cls._userCount = 1
        cls._userDict = {}
