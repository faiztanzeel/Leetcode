var minOperations = function(nums, k) {
    for (let chakra of nums) {
        if (chakra < k) return -1; // Someone too weak
    }
    
    const aboveK = new Set();
    for (let chakra of nums) {
        if (chakra > k) aboveK.add(chakra);
    }
    
    return aboveK.size; // One blast per unique level
};