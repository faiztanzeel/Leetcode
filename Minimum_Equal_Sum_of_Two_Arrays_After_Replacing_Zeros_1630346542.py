/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var minSum = function(nums1, nums2) {
    let sum1 = 0, sum2 = 0;
    let zero1 = 0, zero2 = 0;
    let len = Math.max(nums1.length, nums2.length);

    for (let i = 0; i < len; i++) {
        if (i < nums1.length) {
            if (nums1[i] === 0) {
                zero1++;
                sum1++;
            } else {
                sum1 += nums1[i];
            }
        }

        if (i < nums2.length) {
            if (nums2[i] === 0) {
                zero2++;
                sum2++;
            } else {
                sum2 += nums2[i];
            }
        }
    }

    if ((zero1 === 0 && sum2 > sum1) || (zero2 === 0 && sum1 > sum2)) {
        return -1;
    }

    return Math.max(sum1, sum2);
};