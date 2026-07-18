class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        let res = [];
        nums.sort((a,b) => a - b)
        for(let i = 0; i < nums.length; i++){
            if(i > 0 && nums[i] == nums[i - 1]){
            continue;}
            let r = nums.length - 1;
            let l = i + 1;
            while(l < r){
                let threesum = nums[i] + nums[l] + nums[r];
                if(threesum > 0)
                {
                    r -= 1
                }
                else if(threesum < 0){
                    l += 1
                }
                else{
                    res.push([nums[i],nums[r],nums[l]])
                    l += 1;
                    while(nums[l] == nums[l-1]&& l < r){
                        l += 1;
                    }
                }
            }
        }
        return res;
    }
}
