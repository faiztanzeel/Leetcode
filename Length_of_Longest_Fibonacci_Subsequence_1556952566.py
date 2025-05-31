/**
 * @param {number[]} arr
 * @return {number}
 */
var lenLongestFibSubseq = function(arr) {
    const n = arr.length;
    if (n < 4) { return 0; }
    const keys = new Set(arr);
    let longest = 0;
    
    for (let i = 0; i < n; i++) {
        let first = arr[i];
        for (let j = i + 1; j < n; j++) {
            let second = arr[j];
            let seq = 2;
            let a = first;
            let b = second;
            while (keys.has(a + b)) {
                let next = a + b;
                a = b;
                b = next;
                seq++;
            }
            if (seq > 2) {
                longest = Math.max(longest, seq);
            }
        }
    }
    
    return longest;    
};