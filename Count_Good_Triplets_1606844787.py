/**
 * @param {number[]} arr
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var countGoodTriplets = function(arr, a, b, c) {
    let res = 0;
    let interval = Array(1001).fill(0);  // Prefix count array

    for (let j = 0; j < arr.length; j++) {
        for (let k = j + 1; k < arr.length; k++) {
            if (Math.abs(arr[j] - arr[k]) <= b) {
                let left = Math.max(0, Math.max(arr[j] - a, arr[k] - c));
                let right = Math.min(1000, Math.min(arr[j] + a, arr[k] + c));
                if (left <= right) {
                    if (left === 0)
                        res += interval[right];
                    else
                        res += interval[right] - interval[left - 1];
                }
            }
        }
        for (let ind = arr[j]; ind <= 1000; ind++) {
            interval[ind]++;
        }
    }

    return res;
};