/**
 * @param {string} s
 * @return {number}
 */
var maxDifference = function(s) {
    let freq = Array(26).fill(0);
    for (let ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }

    let mineven = 1000;
    let maxodd = 0;

    for (let count of freq) {
        if (count % 2 === 0 && count > 0) {
            mineven = Math.min(mineven, count);
        } else if (count % 2 !== 0) {
            maxodd = Math.max(maxodd, count);
        }
    }

    return maxodd - mineven;
};