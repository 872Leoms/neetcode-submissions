class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        let stack = []
        for(let n of tokens){
            if(n == '+')
            {
            stack.push(stack.pop() + stack.pop())
            }
            else if(n == '-')
            {
                let a = stack.pop();
                let b = stack.pop();
              stack.push(b - a);
            }
            else if(n == '*')
            {
            stack.push(stack.pop() * stack.pop());
            }
            else if(n == '/')
            {
             let a = stack.pop();
             let b = stack.pop();
             stack.push(Math.trunc(b / a));
            }else{
                stack.push(parseInt(n))
            }
        }
        return stack.pop()
    }
}
