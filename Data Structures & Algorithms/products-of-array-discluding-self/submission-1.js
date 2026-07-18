class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        //let len = nums.length;
        let res = [];
        for(let i = 0; i < nums.length; i++){
           let re = 1;
            for(let j = 0; j < nums.length; j++){
                if(j !== i){
                    re *=  nums[j];
                }
            }
            res.push(re);
        }
        return res;
    }
}
