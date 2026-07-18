class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
      let l = 1;
      let r = Math.max(...piles);
      let speed = r;
      while(l <= r){
        let k = Math.floor((l+r) / 2);
        let m = 0;
        for(let p of piles){
          m += Math.ceil(p / k);
        }
        if(m <= h){
            speed = k;
            r = k - 1;
        }else{
            l = k +1;
        }
      }
      return speed
    }
}
