/**
 * @param {number} n
 * @return {number}
 */
var numTilings = function(n) {
    const MOD = 1000000007;

    const mul = (a, b) => {
        let x = Array(4).fill().map(() => Array(4).fill(0));
        for (let i = 0; i < 4; ++i) {
            for (let j = 0; j < 4; ++j) {
                if (a[i][j]) {
                    for (let k = 0; k < 4; ++k) {
                        if (b[j][k]) {
                            x[i][k] = (x[i][k] + a[i][j] * b[j][k] % MOD) % MOD;
                        }
                    }
                }
            }
        }
        return x;
    };

    let mat = [
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 2, 0, 1],
        [0, 0, 1, 0]
    ];
    let ans = Array(4).fill().map((_, i) => Array(4).fill().map((_, j) => i === j ? 1 : 0));

    while (n > 0) {
        if (n & 1) ans = mul(ans, mat);
        mat = mul(mat, mat);
        n >>= 1;
    }

    return ans[1][1];
};