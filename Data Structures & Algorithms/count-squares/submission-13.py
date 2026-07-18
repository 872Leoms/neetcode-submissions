class CountSquares:

    def __init__(self):
        self.div = {}

    def add(self, point: List[int]) -> None:
        x,y = point 
        if y not in self.div:
            self.div[y] = {}
        if x not in self.div[y]:
            self.div[y][x] = 0
        self.div[y][x] +=  1
        print(self.div)       
    def count(self, point: List[int]) -> int:
        print("start",point)
        x,y = point
        count = 0
        if y not in self.div:
            return count
        for i in self.div[y]:
            if i == x:
                continue
            dif = abs(i - x)
            down = y - dif
            up = y + dif 
            print("iam here",point,down,up,i,dif)
            if down in self.div:
                if x in self.div[down] and i in self.div[down]:
                    temp = 1
                    print("down",self.div[down][x],self.div[down][i])
                    temp *= (self.div[down][x] * self.div[down][i] * self.div[y][i])
                    count += temp
            if up in self.div:
                if x in self.div[up] and i in self.div[up]:
                    temp = 1
                    print("up",self.div[up][x],self.div[up][i])
                    temp *= (self.div[up][x] * self.div[up][i] * self.div[y][i])
                    count += temp
        return(count)
        

        
