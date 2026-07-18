class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            t = str(len(i))
            res += "[" + t + "]" + i 
        return res
    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        temp = ""
        i = 0
        while i < len(s):
            leng = ""
            while s[i] != "]":
                if s[i] != "[":
                    leng += s[i]
                i += 1
            if leng == "0":
                res.append("")
                i += 1
                continue
            t1 = ""
            print(i + int(leng))
            start = i + 1
            d = int(leng) + i + 1
            for j in range(start,d):
                t1 += s[j]
                i = j + 1
            res.append(t1)
        return(res)
            



