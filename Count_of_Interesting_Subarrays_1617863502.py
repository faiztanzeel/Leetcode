/**
 * @param {number[]} nums
 * @param {number} modulo
 * @param {number} k
 * @return {number}
 */
var countInterestingSubarrays = function (nums, modulo, k) {
    const prefixMap = new Map();
    prefixMap.set(0, 1); // prefix mod 0 seen once initially

    let count = 0;
    let res = 0;

    for (const num of nums) {
        if (num % modulo === k) count++;

        const modVal = count % modulo;
        const target = (modVal - k + modulo) % modulo;

        res += prefixMap.get(target) || 0;
        prefixMap.set(modVal, (prefixMap.get(modVal) || 0) + 1);
    }

    return res;
};