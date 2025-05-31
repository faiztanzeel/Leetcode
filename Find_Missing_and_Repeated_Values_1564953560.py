/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findMissingAndRepeatedValues = function(grid) {
    let n = grid.length;
    let n2 = n * n;

    let S = (n2 * (n2 + 1)) / 2;
    let P = (n2 * (n2 + 1) * (2 * n2 + 1)) / 6;

    let S_actual = 0, P_actual = 0;

    for (let row of grid) {
        for (let num of row) {
            S_actual += num;
            P_actual += num * num;
        }
    }

    let diff1 = S_actual - S; // (a - b)
    let diff2 = P_actual - P; // (a^2 - b^2)

    let sum_ab = diff2 / diff1; // (a + b)

    let a = (diff1 + sum_ab) / 2;
    let b = sum_ab - a;

    return [a, b];
};