var colorTheGrid = function(m, n) {
    const MOD = 1e9 + 7;
    const states = [];

    function generate(pos = 0, curr = []) {
        if (pos === m) {
            states.push([...curr]);
            return;
        }
        for (let color = 1; color <= 3; color++) {
            if (pos === 0 || curr[pos - 1] !== color) {
                curr.push(color);
                generate(pos + 1, curr);
                curr.pop();
            }
        }
    }

    generate();

    const size = states.length;
    const transitions = Array.from({ length: size }, () => []);
    for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
            let ok = true;
            for (let k = 0; k < m; k++) {
                if (states[i][k] === states[j][k]) {
                    ok = false;
                    break;
                }
            }
            if (ok) transitions[i].push(j);
        }
    }

    let dp = Array(size).fill(1);
    for (let col = 1; col < n; col++) {
        let newDp = Array(size).fill(0);
        for (let i = 0; i < size; i++) {
            for (const j of transitions[i]) {
                newDp[j] = (newDp[j] + dp[i]) % MOD;
            }
        }
        dp = newDp;
    }

    return dp.reduce((a, b) => (a + b) % MOD, 0);
};