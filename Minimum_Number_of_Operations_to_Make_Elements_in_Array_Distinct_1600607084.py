var minimumOperations = function(nums) {
    let freq = {};
    for (let num of nums) {
        freq[num] = (freq[num] || 0) + 1;
    }

    const isDistinct = () => Object.values(freq).every(v => v <= 1);
    if (isDistinct()) return 0;

    let k = 0;
    while (nums.length > 0) {
        if (nums.length < 3) return k + 1;

        for (let i = 0; i < 3; i++) {
            let val = nums[i];
            freq[val]--;
            if (freq[val] === 0) delete freq[val];
        }

        k++;
        nums = nums.slice(3);
        if (isDistinct()) return k;
    }

    return k;
};