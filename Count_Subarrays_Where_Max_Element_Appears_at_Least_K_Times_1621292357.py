var countSubarrays = function(nums, k) {
    const maxElement = Math.max(...nums);
    let res = 0, left = 0, maxiCount = 0;
    
    for (let right = 0; right < nums.length; right++) {
        if (nums[right] === maxElement) maxiCount++;
        while (maxiCount === k) {
            res += nums.length - right;
            if (nums[left] === maxElement) maxiCount--;
            left++;
        }
    }
    
    return res;
};