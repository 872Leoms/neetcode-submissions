class TimeMap:

    def __init__(self):
        self.dic = dict()
        self.dic2 = dict()
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = {}
        self.dic[key][timestamp] = value
        print(self.dic)
    def get(self, key: str, timestamp: int) -> str: 
        if key not in self.dic or len(self.dic) == 0:
            return ""
        if timestamp in self.dic[key]:
            return self.dic[key][timestamp]
        d = list(self.dic[key].keys())
        print(d)
        if d[0] > timestamp:
            return ""
        l = len(d)
        r = 0
        while True:
            k = (l + r)//2
            if r == l - 1:
                print(d)
                return self.dic[key][d[r]]
            if d[k] > timestamp:
                l = k
            else:
                r = k