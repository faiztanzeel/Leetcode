var robotWithString = function(s) {
    let ans = "";
    let stack = [];
    let freq = new Array(26).fill(0);
    
    for (let char of s) {
        freq[char.charCodeAt(0) - 'a'.charCodeAt(0)]++;
    }
    
    let minChar = 0;
    
    for (let char of s) {
        stack.push(char);
        freq[char.charCodeAt(0) - 'a'.charCodeAt(0)]--;
        
        while (minChar < 26 && freq[minChar] === 0) {
            minChar++;
        }
        
        while (stack.length > 0 && stack[stack.length - 1].charCodeAt(0) - 'a'.charCodeAt(0) <= minChar) {
            ans += stack.pop();
        }
    }
    
    while (stack.length > 0) {
        ans += stack.pop();
    }
    
    return ans;
};