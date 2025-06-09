/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findKthNumber = function(n, k) {
    const count = (n, a, b) => {
        let total = 0;
        while (a <= n){
            total += Math.min(n + 1, b) - a;
            a *= 10;
            b *= 10;
        }
        return total;
    };
    let res = 1;
    k--;
    while (k > 0){
        let steps = count(n, res, res + 1);
        if (steps <= k){
            k -= steps;
            res += 1;
        } else {
            res *= 10;
            k -= 1
        }
    }
    return res;
};