/**
 * @param {number} n
 * @param {number} m
 * @return {number}
 */
var differenceOfSums = function(n, m) {
    let q = Math.floor(n / m); // The divisible numbers can be represented as m * (1 + 2 + ... + q)
    let num2 = m * q * (q + 1) / 2, num1 = n * (n + 1) / 2 - num2;
    return num1 - num2;
}