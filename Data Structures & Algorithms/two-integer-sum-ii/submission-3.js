class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
       let num = new Set(numbers);
       let res = [];
       for(let i = 0; i < numbers.length; i++){
        let thenum = target - numbers[i];
        if(numbers.includes(thenum)){
            res.push((i+1),(numbers.indexOf(thenum) + 1))
            break;
        }     
       }
       console.log(res)
       return(res)
    }
}
