class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length != t.length)return false;
        let st = s.split('').sort().join('');
        let tt = t.split('').sort().join('');
        for(let i = 0; i < s.length; i++){
            if(st[i] != tt[i])return false
        }
        return true
    }
}
