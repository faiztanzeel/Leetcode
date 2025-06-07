String.prototype.removeAtIndex = function(index) {
    if (!this.length) return '';
    return this.slice(0, index) + this.slice(index+1, this.length)
}
/**
 * @param {string} s
 * @return {string}
 */

const BIGGEST_CHAR = 'zz';

var clearStars = function(s) {
    const n = s.length;
    const charMap = {};
    let currentSmallestChar = BIGGEST_CHAR;
    const sArray = Array.from(s);

    const indicesToRemove = [];
    for (let i = 0; i < n; i++) {
        if (s[i] === '*') {
            if (currentSmallestChar !== BIGGEST_CHAR) {
                sArray[charMap[currentSmallestChar].pop()] = '';
                if (charMap[currentSmallestChar].length === 0) {
                    currentSmallestChar = BIGGEST_CHAR;
                    Object.keys(charMap).forEach((c) => {
                        if (currentSmallestChar > c && charMap[c].length) currentSmallestChar = c;
                    });
                }
            }
            indicesToRemove.push(i);
            sArray[i] = '';
        } else {
            if (charMap[s[i]]) charMap[s[i]].push(i)
            else charMap[s[i]] = [i]
            if (currentSmallestChar > s[i]) currentSmallestChar = s[i];
        }
    }

    return sArray.join('');
};