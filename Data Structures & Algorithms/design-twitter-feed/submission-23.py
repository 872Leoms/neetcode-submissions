import heapq
class account:
    def __init__(self):
        self.mytweet = []
        self.folowing = set()
class Twitter:
    def __init__(self):
        self.count = 0
        self.users = {}
    def checkuser(self,idd):
        if idd not in self.users:
            self.users[idd] = account()
        return self.users[idd]
    def postTweet(self, userId: int, tweetId: int) -> None:
        account = self.checkuser(userId)
        self.count += 1
        heapq.heappush(account.mytweet,(-self.count,tweetId))
    def getNewsFeed(self, userId: int) -> List[int]:
        user = self.checkuser(userId)
        feed = []
        following = user.folowing.copy() | {userId}
        for i in following:
            fuser = self.checkuser(i)
            ffeed = fuser.mytweet.copy()
            while ffeed:
                a,b = heapq.heappop(ffeed)
                if len(feed) < 10:
                    heapq.heappush(feed,(-a,b))
                elif -a < feed[0][0]:
                    break
                elif feed[0][0] < -a:
                    heapq.heappop(feed)
                    heapq.heappush(feed,(-a,b))
        res = [] * 10
        while feed:
            f = heapq.heappop(feed)
            res.insert(0,f[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        folloid = self.checkuser(followerId)
        follweeid = self.checkuser(followeeId)
        folloid.folowing.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        folloid = self.checkuser(followerId)
        if followeeId not in folloid.folowing:
            return 
        follweeid = self.checkuser(followeeId)
        folloid.folowing.remove(followeeId)

        
