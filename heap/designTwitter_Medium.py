'''
   (heap) leetcode: 355. Design Twitter (meidum). Company (Twitter)

   Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the `10` most recent tweets in the user's news feed.

   Implement the Twitter class:
      - Twitter() Initializes your twitter object.
      - void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
      - List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
      - void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
      - void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
   

   Example 1:
      Input
         ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
         [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
      Output
         [null, null, [5], null, null, [6, 5], null, [5]]

      Explanation:
         Twitter twitter = new Twitter();
         twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
         twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
         twitter.follow(1, 2);    // User 1 follows user 2.
         twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
         twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
         twitter.unfollow(1, 2);  // User 1 unfollows user 2.
         twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
   

   Constraints:
      - 1 <= userId, followerId, followeeId <= 500
      - 0 <= tweetId <= 10^4
      - All the tweets have unique IDs.
      - At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.

   Related Topics: 
      (Hash table) (linked list) (design) (Heap (Priority queue))
   =============================================================================================

   Solution by myself

   Leetcode submission:
      runtime: 37 ms, beats 95.47%
      memory: 16.4 MB, beats 72.43%
'''
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

from typing import List
from heapq import heapify, heappop, heappush
import math
class Twitter:
   def __init__(self):
      self.timestampTweet = [] # tweetid
      self.usersTweets = {} # userId: [[tweetId, timestamp]]
      self.usersFollow = {} # userId: {followedId...}
      self.timestamp = 0
      pass
   
   # O(1)
   def postTweet(self, userId: int, tweetId: int) -> None:
      self.timestampTweet.append(tweetId)

      if userId in self.usersTweets: 
         self.usersTweets[userId].append([tweetId, self.timestamp])
      else: 
         self.usersTweets[userId] = [[tweetId, self.timestamp]]
      self.timestamp += 1 
   
   # O(5000 log 5000)
   def getNewsFeed(self, userId: int) -> List[int]:
      # make a max heap 
      # get all 10 last tweet from the user and all followed users 
      # while len(heap):
            # pop 10 tweets from the heap as list
            # tweets.append(self.tweetTimestamps[])
      if userId not in self.usersFollow: self.usersFollow[userId] = set()
      users = self.usersFollow[userId]
      users.add(userId)
      maxHeap = []
      heapify(maxHeap)
      for uid in users:
         userTweets = self.usersTweets[uid] if uid in self.usersTweets else []
         startIndex = len(userTweets) - 11
         if startIndex < 0: 
               for [tid, timestamp] in userTweets:
                  heappush(maxHeap, -timestamp)
         else:
               for i in range(startIndex, len(userTweets)):
                  [tweetId, timestamp] = userTweets[i]
                  heappush(maxHeap, -timestamp)
         
      
      recentTweets = [] 
      while len(maxHeap) and len(recentTweets) < 10: 
         recentTweets.append( self.timestampTweet[-heappop(maxHeap)] )

      return recentTweets
   # O(1)
   def follow(self, followerId: int, followeeId: int) -> None:
      if followerId in self.usersFollow: 
         self.usersFollow[followerId].add(followeeId)
      else: 
         self.usersFollow[followerId] = {followeeId}
      pass
   
   # O(1)
   def unfollow(self, followerId: int, followeeId: int) -> None:
      if followerId in self.usersFollow: 
         self.usersFollow[followerId].remove(followeeId)

'''
   input:  ["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed","follow","getNewsFeed","postTweet","follow","getNewsFeed"]
   input:  [[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1],[1,2],[1],[3,1],[3,1],[3]]
   expect: [null,null,[5],null,null,[6,5],null,[5],null,[6,5],null,null,[1,5]]

   input: ["Twitter","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed","follow","getNewsFeed"]
   input: [[],[1,1], [1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[1],[2,21], [2,22], [2,23], [2,24],[2,25],[1],[1,2],[1]]
   expect: [null,null,null,null,null,null,null,null,null,null,null,[10,9,8,7,6,5,4,3,2,1],null,null,null,null,null,[10,9,8,7,6,5,4,3,2,1],null,[25,24,23,22,21,10,9,8,7,6]]

   input: ["Twitter","postTweet","getNewsFeed","follow","getNewsFeed","unfollow","getNewsFeed"]
   input: [[],[1,1],[1],[2,1],[2],[2,1],[2]]

   input: ["Twitter","postTweet","postTweet","unfollow","getNewsFeed"]
   input: [[],[1,4],[2,5],[1,2],[1]]
'''

tw = Twitter() 
tw.postTweet(1,4)
tw.postTweet(2,5)
tw.unfollow(1,2)
print('getNews :', tw.getNewsFeed(1))

# tw = Twitter() 
# tw.postTweet(1,1)
# tw.postTweet(1,2)
# tw.postTweet(1,3)
# tw.postTweet(1,4)
# tw.postTweet(1,5)
# tw.postTweet(1,6)
# tw.postTweet(1,7)
# tw.postTweet(1,8)
# tw.postTweet(1,9)
# tw.postTweet(1,10)
# print('RESULT :', tw.getNewsFeed(1))
# tw.postTweet(2,21)
# tw.postTweet(2,22)
# tw.postTweet(2,23)
# tw.postTweet(2,24)
# tw.postTweet(2,25)
# print('RESULT :', tw.getNewsFeed(1))
# tw.follow(1,2)
# print('RESULT :', tw.getNewsFeed(1))
