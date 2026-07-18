class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        div = {}
        for i in s:
            if i not in  div:
                div[i] = 0
            div[i] += 1
        temp = set()
        res = []
        i = 0
        while i < len(s):
            temp.add(s[i])
            sb = ""
            while temp and (i < len(s)):
                print("we are in what",i)
                k = s[i]
                if k not in temp:
                    temp.add(k)
                div[k] -= 1
                if div[k] == 0:
                    temp.remove(k)
                sb += k
                i += 1
            res.append(sb)
        for d in range(len(res)):
            res[d] = len(res[d])        
        return(res)


            