# Design Twitter

## Summary

Design a simplified Twitter where users can post tweets, follow/unfollow other users, and see the 10 most recent tweets in their news feed.

### Key Points
- Store tweets with timestamps for ordering
- Track follower relationships
- Use a heap to merge tweets from multiple users

### Optimal Approach
Use dictionaries for users and tweets, heap for merging feeds.

```python
import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)  # userId -> [(time, tweetId), ...]
        self.following = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1  # Decrement for max-heap behavior

    def getNewsFeed(self, userId: int) -> list[int]:
        # Include user's own tweets
        users = self.following[userId] | {userId}

        # Collect most recent tweets from each user
        heap = []
        for user in users:
            if self.tweets[user]:
                idx = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][idx]
                heap.append((time, tweetId, user, idx))

        heapq.heapify(heap)

        feed = []
        while heap and len(feed) < 10:
            time, tweetId, user, idx = heapq.heappop(heap)
            feed.append(tweetId)

            if idx > 0:
                idx -= 1
                time, tweetId = self.tweets[user][idx]
                heapq.heappush(heap, (time, tweetId, user, idx))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
```

### Complexity
- postTweet: O(1)
- getNewsFeed: O(k log k) where k is number of users followed
- follow/unfollow: O(1)
- Space: O(users + tweets + follows)

---

## Detailed Explanation

### Problem Analysis

The main challenge is getNewsFeed: we need to merge tweets from multiple users and return the 10 most recent. This is similar to "Merge K Sorted Lists" - each user's tweets are sorted by time, and we merge them.

### Data Structure Design

```
tweets: {
    user1: [(time0, tweet0), (time1, tweet1), ...],
    user2: [(time0, tweet0), ...],
    ...
}

following: {
    user1: {user2, user3},
    user2: {user1},
    ...
}
```

### News Feed Algorithm

1. Get all users whose tweets should appear (followees + self)
2. Add each user's most recent tweet to a max-heap
3. Pop from heap, add to feed
4. Push the popped user's next most recent tweet (if any)
5. Repeat until 10 tweets or heap empty

This is exactly the k-way merge pattern.

### Why Decrement Time?

Python's heapq is a min-heap. By using negative/decreasing timestamps, smaller values (more negative = more recent) come first, simulating a max-heap.

### Alternative: Store All Tweets Globally

```python
class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = []  # [(time, userId, tweetId), ...]
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((self.time, userId, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        users = self.following[userId] | {userId}
        feed = []

        for time, user, tweetId in reversed(self.tweets):
            if user in users:
                feed.append(tweetId)
                if len(feed) == 10:
                    break

        return feed
```

- getNewsFeed: O(total tweets) worst case
- Simpler but less efficient for many tweets

### Edge Cases
- User with no tweets: empty feed
- User follows no one: only their own tweets
- User unfollows themselves: should not affect feed
- More than 10 tweets available: return only 10

### Related Problems
- Merge K Sorted Lists: same merge pattern
- Design Search Autocomplete System: similar design problem
- Design a Leaderboard: ranking with updates
