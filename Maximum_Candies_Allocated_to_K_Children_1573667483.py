var maximumCandies = function(candies, k) {
    // Function to check if 'val' candies can be distributed to at least 'k' children
    const solve = (candies, k, val) => {
        let totalPieces = 0; // Track total number of candy pieces
        
        // Iterate through each candy count
        for (let candy of candies) {
            if (val <= candy) { // Only count valid pieces
                totalPieces += Math.floor(candy / val); 
            }
        }
        return totalPieces >= k; // Return true if enough pieces are possible
    };

    // Sort the candies array for efficient binary search
    candies.sort((a, b) => a - b);
    let start = 1, end = candies[candies.length - 1], answer = 0;

    // Binary search to find the maximum number of candies per child
    while (start <= end) {
        let mid = Math.floor((start + end) / 2); // Calculate mid value

        if (solve(candies, k, mid)) {
            answer = mid; // Update valid answer
            start = mid + 1; // Try for larger values
        } else {
            end = mid - 1; // Reduce search range
        }
    }
    return answer; // Return the maximum valid answer
};