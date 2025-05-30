var countGoodNumbers = function(n) {
    const MOD = 1_000_000_007n;

    function modPow(base, exp, mod) {
        let result = 1n;
        base = BigInt(base);
        exp = BigInt(exp);
        while (exp > 0n) {
            if (exp % 2n === 1n)
                result = (result * base) % mod;
            base = (base * base) % mod;
            exp = exp / 2n;
        }
        return result;
    }

    const even = BigInt((BigInt(n) + 1n) / 2n);
    const odd = BigInt(n) / 2n;
    const pow5 = modPow(5, even, MOD);
    const pow4 = modPow(4, odd, MOD);

    return Number((pow5 * pow4) % MOD);
};