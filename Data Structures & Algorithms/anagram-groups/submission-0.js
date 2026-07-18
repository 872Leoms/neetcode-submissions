class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let res = {};
        for(let word of strs){
           let arr = new Array(26).fill(0);
           for(let n of word){
            arr[n.charCodeAt(0) - 'a'.charCodeAt(0)] +=1
           }
           let jo = arr.join(',');
           if(!res[jo]){
            res[jo] = [];
           }
           res[jo].push(word);
        }
        console.log(Object.values(res));
        return Object.values(res);
    }
}
