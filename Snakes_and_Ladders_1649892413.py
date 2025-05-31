/**
 * @param {number[][]} board
 * @return {number}
 */
var snakesAndLadders = function(board) {
    const n = board.length;
    const cell = new Array(n * n).fill(-1);

    for (let i = n - 1; i >= 0; i -= 2) {
        for (let j = 0; j < n; j++) {
            cell[(n - 1 - i) * n + j] = board[i][j] - 1;
            if (i - 1 >= 0) {
                cell[(n - i) * n + (n - 1 - j)] = board[i - 1][j] - 1;
            }
        }
    }

    const visited = new Array(n * n).fill(-1);
    const queue = [];
    queue.push(0);
    visited[0] = 0;

    while (queue.length > 0) {
        const curr = queue.shift();
        if (curr === n * n - 1) {
            return visited[curr];
        }
        const maxStep = Math.min(6, n * n - 1 - curr);
        for (let i = 1; i <= maxStep; i++) {
            let nextPos = curr + i;
            if (cell[nextPos] !== -2) {
                nextPos = cell[nextPos];
            }
            if (visited[nextPos] === -1) {
                visited[nextPos] = visited[curr] + 1;
                queue.push(nextPos);
            }
        }
    }

    return -1;
};