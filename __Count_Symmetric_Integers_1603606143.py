var countSymmetricIntegers = function(low, high) {
    let count = 0;
    for (let num = low; num <= high; num++) {
        const s = num.toString();
        if (s.length % 2 === 0) {
            const mid = s.length / 2;
            const leftSum = [...s.slice(0, mid)].reduce((a, b) => a + +b, 0);
            const rightSum = [...s.slice(mid)].reduce((a, b) => a + +b, 0);
            if (leftSum === rightSum) count++;
        }
    }
    return count;
};