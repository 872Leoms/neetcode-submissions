class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        let f = {};
        for(let l of s1){
            f[l] = (f[l] || 0) + 1;
        }
        let thelength = Object.keys(f).length;
        for(let i = 0; i < s2.length; i++){
            let second = {};
            let currnut = 0;
            for(let j = i; j < s2.length; j++){
                let c = s2[j];
                second[c] = (second[c] || 0) + 1;

                if((f[c] || 0) < second[c]){
                    break;
                }
                if((f[c] || 0) === second[c]){
                    currnut++
                }
                if(currnut == thelength){
                    return true;
                }
            }

        }
        return false;
    }
}
