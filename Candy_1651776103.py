/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function(ratings) {
    const n = ratings.length;
    const c = new Array(n).fill(1);
    let cnt = 0;
    for (let i = 1; i < n; i++){
        if (ratings[i] > ratings[i - 1]){
            c[i] = c[i - 1] + 1;
        }
    }
    for (let i = n - 1; i > 0; i--){
        if (ratings[i - 1] > ratings[i]){
            c[i - 1] = Math.max(c[i] + 1, c[i - 1]);
        }
        cnt += c[i - 1];
    }
    return cnt + c[n - 1];
};