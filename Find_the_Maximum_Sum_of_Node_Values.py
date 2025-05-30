/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number[][]} edges
 * @return {number}
 */
var maximumValueSum = function(nums, k, edges) {
    let total = 0;
    let n = 0;
    let minDiff = 1 << 30;
    for (let x of nums){
        let y = x ^ k;
        total += Math.max(x, y);
        if (x < y){
            n = 1 - n;
        }
        minDiff = Math.min(minDiff, Math.abs(x - y));
    }
    return total - n * minDiff;
};