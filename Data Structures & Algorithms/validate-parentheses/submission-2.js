class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let stack = [];
        let map = {
            '}': '{',
            ']': '[',
            ')': '(',
        };
        for(let char of s){
           // let isBracket = char in map;
            if(!(char in map)){
             stack.push(char);
             }else{
                if(stack[stack.length -1] == map[char] && stack.length >= 1){
                    stack.pop()
                }else{
                    return false
                }
             }
         }
        console.log(stack)
        return stack.length === 0;
      }
    }
