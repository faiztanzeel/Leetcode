var numRabbits = function(answers) {
    const count = {};
    for (let a of answers) count[a] = (count[a] || 0) + 1;

    let res = 0;
    for (let [k, v] of Object.entries(count)) {
        let x = parseInt(k);
        res += Math.ceil(v / (x + 1)) * (x + 1);
    }
    return res;
};