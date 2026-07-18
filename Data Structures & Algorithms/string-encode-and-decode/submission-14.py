class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += i + "§"
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        temp = ""
        for i in s:
            if i =="§":
                res.append(temp)
                temp = ""
            else:
                temp += i
        return res
            

