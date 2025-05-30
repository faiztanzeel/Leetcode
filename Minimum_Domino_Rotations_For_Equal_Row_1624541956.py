function minDominoRotations(tops, bottoms) {
    let cnta = Array(7).fill(0), cntb = Array(7).fill(0), same = Array(7).fill(0);
    for (let i = 0; i < tops.length; i++) {
        cnta[tops[i]]++;
        cntb[bottoms[i]]++;
        if (tops[i] === bottoms[i]) same[tops[i]]++;
    }
    for (let i = 1; i <= 6; i++) {
        if (cnta[i] + cntb[i] - same[i] === tops.length) {
            return Math.min(cnta[i], cntb[i]) - same[i];
        }
    }
    return -1;
}