function distributeCandies(n, limit) {
    let dp = Array(n + 1).fill(0);
    dp[0] = 1;
    for (let p = 0; p < 3; ++p) {
        let newDp = Array(n + 1).fill(0);
        let prefix = Array(n + 2).fill(0);
        for (let i = 0; i <= n; ++i)
            prefix[i + 1] = prefix[i] + dp[i];
        for (let i = 0; i <= n; ++i) {
            let l = Math.max(0, i - limit), r = i;
            newDp[i] = prefix[r + 1] - prefix[l];
        }
        dp = newDp;
    }
    return dp[n];
}