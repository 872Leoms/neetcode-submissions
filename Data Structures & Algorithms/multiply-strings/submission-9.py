class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [i*0 for i in range(len(num1) + len(num2))] 
        div = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        div2 = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}

        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                r1 = div[num1[i]]
                r2 = div[num2[j]]
                temp = r1 * r2
                one = temp % 10
                ten = temp // 10
                res[i + j + 1 ] += one
                if res[i + j + 1] > 9:
                    ten += res[i + j + 1] //  10
                    res[i + j + 1] =  res[ i + j + 1] % 10
                res[i+j] += ten
    
        """for i in range(len(res)-1,-1,-1):
            if res[i] > 9:
                t1 = res[i]
                res[i] = t1 % 10
                res[i-1] += t1 // 10"""
        fi = ""
        print(res)
        for i in range(len(res)):
            if res[i] != 0:
                for j in range(i,len(res)):
                    fi += div2[res[j]]
                break
        if not fi:
            return "0"
        return(fi)                   



