/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumTripletValue = function(nums) {
    let maxProduct = 0;
    let maxDiff = 0;
    let maxNum = 0;

    for (let num of nums) {
        maxProduct = Math.max(maxProduct, maxDiff * num);
        maxNum = Math.max(maxNum, num);
        maxDiff = Math.max(maxDiff, maxNum - num);
    }

    return maxProduct;
};