class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let num = new Set(nums);
        let res = 0;
        for(let i of num){
            let s = 0;
            let c = i;
            while(num.has(c)){
                s++;
                c++;
            }
            res = Math.max(s,res)
        }
        return res;
    }
}
