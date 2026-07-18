
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = []
        def recursion(cur,cl,op,n):
            if cl == op == n:
                temp.append(cur)
            else:
                if op > cl and op == n:
                    recursion(cur + ")",cl+1,op,n)
                elif op == cl and cl !=n:
                    (recursion(cur + "(",cl,op+1,n))
                elif op > cl:
                    recursion(cur + ")",cl+1,op,n)
                    recursion(cur + "(",cl,op+1,n)
        recursion("",0,0,n)
        return(temp)
