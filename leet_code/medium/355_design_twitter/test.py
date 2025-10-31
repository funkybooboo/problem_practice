import unittest
from solution import Twitter


class TestTwitter(unittest.TestCase):

    def test_example_scenario(self):
        twitter = Twitter()
        twitter.postTweet(1, 5)  # User 1 posts tweet 5
        self.assertEqual(twitter.getNewsFeed(1), [5])

        twitter.follow(1, 2)  # User 1 follows user 2
        twitter.postTweet(2, 6)  # User 2 posts tweet 6
        self.assertEqual(twitter.getNewsFeed(1), [6, 5])

        twitter.unfollow(1, 2)  # User 1 unfollows user 2
        self.assertEqual(twitter.getNewsFeed(1), [5])

    def test_multiple_tweets_and_follows(self):
        twitter = Twitter()
        twitter.postTweet(1, 101)
        twitter.postTweet(2, 102)
        twitter.postTweet(1, 103)
        twitter.postTweet(3, 104)
        twitter.postTweet(2, 105)
        twitter.follow(1, 2)
        twitter.follow(1, 3)

        news_feed = twitter.getNewsFeed(1)
        self.assertEqual(news_feed, [105, 104, 103, 102, 101])

    def test_limit_news_feed_to_10(self):
        twitter = Twitter()
        for i in range(15):
            twitter.postTweet(1, i)
        self.assertEqual(twitter.getNewsFeed(1), list(range(14, 4, -1)))

    def test_unfollow_self_no_effect(self):
        twitter = Twitter()
        twitter.postTweet(1, 42)
        twitter.unfollow(1, 1)  # Should not cause error or remove tweets
        self.assertEqual(twitter.getNewsFeed(1), [42])

    def test_follow_idempotency(self):
        twitter = Twitter()
        twitter.follow(1, 2)
        twitter.follow(1, 2)
        twitter.postTweet(2, 99)
        self.assertEqual(twitter.getNewsFeed(1), [99])

    def test_unfollow_non_followed(self):
        twitter = Twitter()
        twitter.postTweet(2, 88)
        twitter.unfollow(1, 2)  # No-op
        self.assertEqual(twitter.getNewsFeed(1), [])


if __name__ == "__main__":
    unittest.main()
