class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let l = 0, r = 1;
        let maxp = 0;
        while(r < prices.length){
          if(prices[r] > prices[l]){
            let prof = prices[r]  - prices[l];
            maxp =Math.max(maxp, prof)
          }else{
            l = r;
          }
          r++;
        }
        return maxp;
    }
}
