class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
       let r = nums.length - 1;
        let l = 0;
        while(l < r){
           let m = l + Math.floor((r - l) / 2);
            if(nums[m] < nums[r]){
                r = m;
            }else{
                l = m + 1;
            }
        }
        return nums[l];
    }
}
