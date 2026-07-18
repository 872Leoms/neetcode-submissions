class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
       let  m = matrix.length;
       let  n = matrix[0].length;
       for(let c of matrix){
         if(target >= c[0] || target <= c[n-1]){
            for(let n of c){
                if(target == n )return true
            }
         }
       }
       return false
    }
}
