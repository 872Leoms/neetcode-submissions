class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dec = dict()
        visited = set()

        def rec(j,arr):
            if j not in dec.keys():
                print("we are in j not in dec")
                return True
            if j in arr:
                print("we are in return false")
                return False
            visited.add(j)
            temp = arr + [j]
            for i in dec[j]:
               if not  rec(i,temp):
                return False
            return True
        
        for i in prerequisites:
            one = i[0]
            two = i[1]
            if one in dec:
                dec[one].append(two)
            else:
                dec[one] = [two]
        print(dec)
        for j in dec.keys():
            if j not in visited:
                if not (rec(j,[])):
                    return False
        return True

        