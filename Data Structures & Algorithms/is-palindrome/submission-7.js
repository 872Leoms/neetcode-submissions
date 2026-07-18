class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let com = '';
        let com2 = s.replace(/[\s?!"',.:]/g, '').toLowerCase();
        console.log(com2)
        for(let i = com2.length - 1; i >= 0; i--){
           com += com2[i];
        }
        if(com !== com2)return false;
        return true;
    }
}
