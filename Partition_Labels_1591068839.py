var partitionLabels = function(s) {
    let freq = new Array(26).fill(0);
    let a = 'a'.charCodeAt(0);

    for (let char of s) {
        freq[char.charCodeAt(0) - a]++;
    }

    let output = [];
    let prevEnd = 0;

    function isValid(start, end) {
        for (let i = start; i <= end; i++) {
            if (freq[s.charCodeAt(i) - a] !== 0) return false;
        }
        return true;
    }

    for (let i = 0; i < s.length; i++) {
        freq[s.charCodeAt(i) - a]--;

        if (isValid(prevEnd, i)) {
            output.push(i - prevEnd + 1);
            prevEnd = i + 1;
        }
    }

    return output;
};