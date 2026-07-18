class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc","3": "def","4": "ghi","5": "jkl",
            "6": "mno","7": "qprs","8": "tuv","9": "wxyz",}
        def rec(digits,ind,per):
            if len(per) == len(digits):
                if per:
                    res.append(per)
                return
            else:
                thestring = digitToChar[digits[ind]]
                for i in thestring:
                    rec(digits,ind+1,per+i)
        rec(digits,0,"")
        return(res)