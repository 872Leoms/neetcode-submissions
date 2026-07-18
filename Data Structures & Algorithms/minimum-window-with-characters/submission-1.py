class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lengths = dict()
        for i in range(len(s)):
            temp = list(t)
            count = s[i]
            steps = 1
            length = len(t)
            d = i + 1
            if s[i] in temp:
                length -= 1
                temp.remove(s[i])
            while length > 0 and d < len(s):
                if s[d] in temp:
                    length -= 1
                    temp.remove(s[d])
                count += s[d]
                steps += 1
                d += 1
            if length == 0:
                lengths[steps] = count
        if len(lengths.keys()) == 0:
            lengths[0] = ""
        return(lengths[min(lengths.keys())])
        