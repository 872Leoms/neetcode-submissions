class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        div = {}
        visited = set()
        stack = []
        j = 0
        for i in edges:
            a,b = i
            if a not in div:
                div[a] = []
            if b not in div:
                div[b] = []
            div[a].append(b)
            div[b].append(a)
        count = 0
        lastt = set()
        for j in range(n):
            if j in visited:
                continue
            count += 1
            stack.append(j)
            while stack:
                k = stack.pop()
                visited.add(k)
                if k in div:
                    for i in div[k]:
                        if i not in visited:
                            stack.append(i)
                lastt.add(k)
        return(count)
            
                
        