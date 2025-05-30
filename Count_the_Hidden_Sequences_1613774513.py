var numberOfArrays = function(differences, lower, upper) {
    let minSum = 0, maxSum = 0, sum = 0;
    for (let diff of differences) {
        sum += diff;
        minSum = Math.min(minSum, sum);
        maxSum = Math.max(maxSum, sum);
    }
    const count = (upper - maxSum) - (lower - minSum) + 1;
    return count > 0 ? count : 0;
};