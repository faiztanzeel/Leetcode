/**
 * @param {number} n
 * @return {number[]}
 */
var lexicalOrder = function(n) {
    let res = new Array(n);
    let curr = 1;
    for( let i = 0; i < n; i++){
        res[i] = curr;
        if (curr * 10 > n){
            if (curr === n){
                curr = Math.floor(curr / 10);
            }
            curr++;
            while (curr % 10 === 0){
                curr = Math.floor(curr / 10);
            }
        } else {
            curr *= 10;
        }
    }
    return res;
};