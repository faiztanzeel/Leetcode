/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countPairs = function(nums, k) {
    const indexMap = new Map();
    let count = 0;

    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        if (indexMap.has(num)) {
            for (const j of indexMap.get(num)) {
                if ((i * j) % k === 0) {
                    count++;
                }
            }
        }
        if (!indexMap.has(num)) {
            indexMap.set(num, []);
        }
        indexMap.get(num).push(i);
    }

    return count;
};