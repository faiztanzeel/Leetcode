var findEvenNumbers = function(digits) {
    let freq = new Array(10).fill(0);
    for (let d of digits) freq[d]++;
    
    let res = [];
    for (let i = 100; i <= 998; i += 2) {
        let a = Math.floor(i / 100), b = Math.floor(i / 10) % 10, c = i % 10;
        let local = new Array(10).fill(0);
        local[a]++; local[b]++; local[c]++;
        let valid = true;
        for (let j = 0; j < 10; j++) {
            if (local[j] > freq[j]) {
                valid = false;
                break;
            }
        }
        if (valid) res.push(i);
    }
    return res;
};