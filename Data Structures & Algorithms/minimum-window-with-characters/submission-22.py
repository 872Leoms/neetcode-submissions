class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        d = -1
        res = []
        shortest = s
        have = 0
        temp = dict()
        check = dict()
        l = float('inf')
        r = 0
        for i in t:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        need = len(temp.keys())
        for i in range(len(s)):
            if s[i] in temp and s.count(s[i]) < temp[s[i]]:
                return ""
            if i != 0:
                check[s[i-1]] -= 1
                if s[i-1] in temp and check[s[i-1]] < temp[s[i-1]]:
                     have -= 1
            if((len(s) - i) < len(t)):
                break
            while need > have:
                if d == len(s) - 1:
                    break
                d += 1
                if s[d] not in check:
                    check[s[d]] = 1
                else:
                    check[s[d]] += 1
                if s[d] in temp and check[s[d]] == temp[s[d]]:
                     have += 1
            if(have == need):
                if (d - i + 1) < l:
                    l = d-i+1
                    r = i
        if l == float("inf"):
            return ""
        return(s[r:r+l])
