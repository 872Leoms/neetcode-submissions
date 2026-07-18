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
            if(st != tt)return false
        return true
    }
}
