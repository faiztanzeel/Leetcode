var isZeroArray = function(nums, queries, mid) {
    let n = nums.length;
    let temp = [...nums];
    let delta = new Array(n + 1).fill(0);

    for (let i = 0; i < mid; i++) {
        let [l, r, v] = queries[i];
        delta[l] -= v;
        if (r + 1 < n) delta[r + 1] += v;
    }

    let currDecrement = 0;
    for (let i = 0; i < n; i++) {
        currDecrement += delta[i];
        temp[i] += currDecrement;
        if (temp[i] > 0) return false;
    }
    return true;
};

var minZeroArray = function(nums, queries) {
    let left = 0, right = queries.length, ans = -1;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        if (isZeroArray(nums, queries, mid)) {
            ans = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return ans;
};