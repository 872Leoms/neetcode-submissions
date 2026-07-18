class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        let stack = [];
        for(let f = 0; f < temperatures.length; f++){
            let s = 0;
            for(let num = f + 1; num < temperatures.length; num++){
                if(temperatures[num] > temperatures[f]){
                    s += num - f;
                    break;
                }
            }
            stack.push(s)
        }
        console.log(temperatures)
        console.log(stack)
        return stack
    }
}
