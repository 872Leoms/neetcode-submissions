class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target, position, speed) {
      let pair = position.map((p,i) => [p,speed[i]]);
      pair.sort((a,b) => b[0] - a[0]);
      let fleets = 1;
      let prev = (target - pair[0][0]) / pair[0][1];
      for(let i = 1; i < pair.length; i++){
        let m = (target - pair[i][0]) / pair[i][1]
        if(m > prev){
            fleets++
            prev = m
        }
      }
       return fleets;
    }
}
