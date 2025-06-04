function answerString(word, friends) {
    if (friends === 1) return word;
    let res = '';
    for (let i = 0, n = word.length, m = n - friends + 1; i < n; i++) {
        const part = word.substring(i, i + m);
        if (part > res) res = part;
    }
    return res;
}