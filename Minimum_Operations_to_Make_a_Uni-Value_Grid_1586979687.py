var minOperations = function(grid, x) {
    let all = grid.flat();
    let mod = all[0] % x;

    for (let num of all) {
        if (num % x !== mod) return -1;
    }

    all.sort((a, b) => a - b);
    let median = all[Math.floor(all.length / 2)];
    let operations = 0;

    for (let num of all) {
        operations += Math.abs(num - median) / x;
    }

    return operations;
};