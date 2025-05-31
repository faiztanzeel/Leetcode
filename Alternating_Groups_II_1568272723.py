var numberOfAlternatingGroups = function(colors, k) {
    colors.push(...colors.slice(0, k - 1)); 
    let count = 0;
    let left = 0;
    
    for (let right = 0; right < colors.length; right++) {
        if (right > 0 && colors[right] === colors[right - 1]) {
            left = right;  
        }
        
        if (right - left + 1 >= k) {
            count++;  
        }
    }
    
    return count;
};