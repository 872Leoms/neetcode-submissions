class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let num = {};
        for(let n of nums)
        {
            num[n] = (num[n] || 0) + 1;
        }
        let rr = Object.entries(num).map(([num, freq]) => [freq, parseInt(num)]);
        rr.sort((a,b) => b[0] - a[0]);
        return rr.slice(0, k).map(pair => pair[1]);
    }
}
