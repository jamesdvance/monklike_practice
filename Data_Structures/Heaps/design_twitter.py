# Using A Heap
from collections import defaultdict 
import heapq

class Twitter:

    def __init__(self):
        self._user_feeds = defaultdict(list) # {user_id (int): feed: List[tup] (time, tweetId, userId)}
        self._followers = defaultdict(set) # {user_id (int): followers List[int] }
        self._user_tweets = defaultdict(list) # {user_id (int): tweets List[tup] (time, tweetId, userId)}
        self._time= 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        " Inserts into all feeds "
        self._time -=1 
        # Add to author's tweets
        self._user_tweets[userId].append((self._time, tweetId, userId))
        # Add to author's feed (own tweets should always be in feed)
        self._user_feeds[userId].append((self._time, tweetId, userId))

        # Push to follower's timelines
        for follower in self._followers[userId]:
            if self._user_feeds[follower] == []:
                heapq.heapify(self._user_feeds[follower])
            heapq.heappush(self._user_feeds[follower], (self._time, tweetId, userId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        """ Get 10 Most Recent"""
        return [tweet[1] for tweet in heapq.nsmallest(10, self._user_feeds[userId]) ]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        # Add follower to followee's followers
        if followerId not in self._followers[followeeId]:
            self._followers[followeeId].add(followerId)
            if self._user_feeds[followerId] == []:
                heapq.heapify(self._user_feeds[followerId])
            # push all tweets from followee into this follower's feed
            for tweet in self._user_tweets[followeeId]:
                heapq.heappush(self._user_feeds[followerId], tweet)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove follower from followee's followers
        if followerId in self._followers[followeeId]:
            self._followers[followeeId].remove(followerId)
        # remove followee's tweets from follower's feed
        new_feed = [itm for itm in self._user_feeds[followerId] if itm[2] != followeeId] 
        heapq.heapify(new_feed)
        self._user_feeds[followerId] = new_feed


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)