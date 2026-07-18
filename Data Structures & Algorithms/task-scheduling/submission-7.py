class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        temp = [0] * 26
        maxx = 0
        countt = 0
        for i in tasks:
            k = ord(i) - ord("A")
            temp[k] += 1
        for i in temp:
            if i > maxx:
                maxx = i
        for i in temp:
            if i == maxx:
                countt += 1
        return(max(len(tasks),((maxx - 1) * (n+1) + countt)))
        print(maxx)
        print(temp)

        