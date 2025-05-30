var countBalancedPermutations = function(num) {
    const digits = num.split('');
    const results = new Set();
    const used = Array(digits.length).fill(false);
    let count = 0;

    const backtrack = (path) => {
        if (path.length === digits.length) {
            const key = path.join('');
            if (!results.has(key)) {
                results.add(key);
                let evenSum = 0, oddSum = 0;
                for (let i = 0; i < path.length; i++) {
                    if (i % 2 === 0) evenSum += +path[i];
                    else oddSum += +path[i];
                }
                if (evenSum === oddSum) count++;
            }
            return;
        }

        for (let i = 0; i < digits.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            path.push(digits[i]);
            backtrack(path);
            path.pop();
            used[i] = false;
        }
    };

    backtrack([]);
    return count;
};