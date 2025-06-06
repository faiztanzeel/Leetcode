/**
 * @param {number} n
 * @return {boolean}
 */
var checkPowersOfThree = function(n) {
    while (n > 0) {
        if (n % 3 > 1) return false;
        n = Math.floor(n / 3);
    }
    return true;
};