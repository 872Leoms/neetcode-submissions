class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let res = -1;
        for(let n = 0; n < nums.length; n++){
         if(nums[n] == target){
            res = n;
         }
        }
        if(res == -1)return -1;
        return res;
    }
}
