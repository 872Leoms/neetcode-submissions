class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxx = 0
        div = {}
        curr = 0
        p = 0
        for i in range(len(s)):
            total = i - curr +1
            if s[i] not in div:
                div[s[i]] = 0
            div[s[i]] += 1
            p = max(div.values())
            if total - p > k:
                while total - p > k:
                    maxx = total - 1 if total-1 > maxx else maxx
                    div[s[curr]] -= 1
                    curr += 1
                    total = i - curr +1
        maxx = total  if total > maxx else maxx
        return(maxx)
                    




