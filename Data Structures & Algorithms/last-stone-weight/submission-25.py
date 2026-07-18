class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def heapfiy(stone,i):
            if i == len(stone)-1:
                return stone
            largest = i
            left = (2 * i) + 1
            right = (2 * i) + 2
            if left < len(stone) and stone[left] > stone[i]:
                largest = left
            if right < len(stone) and stone[right] > stone[largest]:
                largest = right
            if largest == i:
                return
            stone[largest],stone[i] = stone[i],stone[largest] 
            heapfiy(stones,largest)
        def heapfiyup(arr,i):
            if i == 0:
                return arr
            theparent = (i-1) // 2
            largest = theparent
            if theparent < len(arr) and arr[theparent] < arr[i]:
                largest = i
            if largest == theparent:
                return arr
            arr[largest],arr[theparent] = arr[theparent],arr[largest]
            return heapfiyup(arr,theparent)
            
        def extraxtmax(arr):
            if len(arr) < 2:
                return arr.pop()
            arr[0],arr[-1] = arr[-1],arr[0]
            maxx = arr.pop()
            heapfiy(arr,0)
            return maxx
        for i in range((len(stones) // 2) -1,-1,-1):
            heapfiy(stones,i)
        
        temp = stones
        while temp and len(temp) > 1:
            print("wow")
            print(temp)
            flargest = extraxtmax(temp)
            slargest = extraxtmax(temp)
            print(temp)
            smash = abs(flargest - slargest)
            if smash > 0:
                temp.append(smash)
                temp = heapfiyup(temp,len(temp)-1)
            print(temp)
        if temp:
            return temp[0]
        return 0
