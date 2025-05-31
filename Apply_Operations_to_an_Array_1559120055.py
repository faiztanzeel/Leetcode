/**
 * @param {number[]} nums
 * @return {number[]}
 */
var applyOperations = function(nums) {
    const n = nums.length;
    
    // Apply operations
    for (let i = 0; i < n - 1; i++) {
        if (nums[i] === nums[i + 1]) {
            nums[i] *= 2;
            nums[i + 1] = 0;
        }
    }
    
    // Shift zeros to the end (in-place)
    let nonZeroIdx = 0;
    
    // Move all non-zero elements to the front
    for (let i = 0; i < n; i++) {
        if (nums[i] !== 0) {
            nums[nonZeroIdx++] = nums[i];
        }
    }
    
    // Fill the remaining positions with zeros
    while (nonZeroIdx < n) {
        nums[nonZeroIdx++] = 0;
    }
    
    return nums;
};