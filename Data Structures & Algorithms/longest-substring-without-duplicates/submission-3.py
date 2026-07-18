class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = []
        length = []
        for i in s:
            if i in temp:
                while i in temp:
                    length.append(len(temp))
                    temp = temp[1:]
                else:
                    temp.append(i)
            else:
                temp.append(i)
        length.append(len(temp))
        print(temp)
        print(length)
        return max(length)
                
        