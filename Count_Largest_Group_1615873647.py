var countLargestGroup = function(n) {
    let map = new Array(40).fill(0);
    let max = 0, ans = 0;

    for (let i = 1; i <= n; i++) {
        let sum = 0, num = i;
        while (num > 0) {
            sum += num % 10;
            num = Math.floor(num / 10);
        }
        map[sum]++;
        if (map[sum] > max) {
            max = map[sum];
            ans = 1;
        } else if (map[sum] === max) {
            ans++;
        }
    }

    return ans;
};