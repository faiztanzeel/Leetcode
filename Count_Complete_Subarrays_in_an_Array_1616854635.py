/**
 * @param {number[]} nums
 * @return {number}
 */
var countCompleteSubarrays = function(nums) {
    const totalUnique = new Set(nums).size;
    const freq = new Map();
    let left = 0, unique = 0, res = 0;

    for (let right = 0; right < nums.length; right++) {
        freq.set(nums[right], (freq.get(nums[right]) || 0) + 1);
        if (freq.get(nums[right]) === 1) unique++;

        while (unique === totalUnique) {
            res += nums.length - right;
            freq.set(nums[left], freq.get(nums[left]) - 1);
            if (freq.get(nums[left]) === 0) unique--;
            left++;
        }
    }
    return res;
};