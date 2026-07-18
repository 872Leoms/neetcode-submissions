class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        div = {}
        for i in edges:
            a,b = i
            if a == b:
                return False
            if a not in div:
                div[a] = []
            if b not in div:
                div[b] = []
            div[a].append(b)
            div[b].append(a)

        stack = [[0,None]]
        visited = set()
        def rec(stack,visited):
            print("we are start")
            if not stack:
                print("we are in ")
                return True
            k,p = stack.pop()
            print("k,p",k,p)
            if k in visited and k != p:
                print("false",stack,visited,p)
                return False
            visited.add(k)
            print("visited",visited)
            if k in div:
                for i in div[k]:
                    if i not in visited:
                        stack.append([i,k])
            return rec(stack,visited)


        if rec(stack,visited) and len(visited) == n:
            return True
        print("false here")
        return False

        