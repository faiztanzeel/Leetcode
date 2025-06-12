/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAdjacentDistance = function(nums) {
    let maxDist = 0;
    
    // Check adjacent elements
    for(let i = 1; i < nums.length; i++) {
        maxDist = Math.max(maxDist, Math.abs(nums[i] - nums[i-1]));
    }
    
    // Check wrap-around
    maxDist = Math.max(maxDist, Math.abs(nums[0] - nums[nums.length-1]));
    
    return maxDist;
};