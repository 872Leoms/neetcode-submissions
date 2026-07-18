class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let res = 0;
        for(let i = 0; i < heights.length-1; i++){
            for(let j = i + 1; j < heights.length; j++){
               let k = (Math.min(heights[i],heights[j])) * (j - i);
               res = Math.max(res,k);
            }
        }
        return(res)
    }
}
