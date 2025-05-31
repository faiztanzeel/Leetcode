/**
 * @param {number[][]} nums1
 * @param {number[][]} nums2
 * @return {number[][]}
 */
var mergeArrays = function(nums1, nums2) {
    // Initialize pointers for both arrays
    let i = 0, j = 0;
    const result = [];
    
    // Traverse both arrays with two pointers
    while (i < nums1.length && j < nums2.length) {
        const [id1, val1] = nums1[i];
        const [id2, val2] = nums2[j];
        
        if (id1 < id2) {
            // Id1 is smaller, add it to result
            result.push([id1, val1]);
            i++;
        } else if (id2 < id1) {
            // Id2 is smaller, add it to result
            result.push([id2, val2]);
            j++;
        } else {
            // Ids are equal, sum the values
            result.push([id1, val1 + val2]);
            i++;
            j++;
        }
    }
    
    // Add remaining elements from nums1, if any
    while (i < nums1.length) {
        result.push(nums1[i]);
        i++;
    }
    
    // Add remaining elements from nums2, if any
    while (j < nums2.length) {
        result.push(nums2[j]);
        j++;
    }
    
    return result;
};