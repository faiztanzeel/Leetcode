function countGoodIntegers(n, k) {
  const start = Math.pow(10, n - 1);
  const end = Math.pow(10, n) - 1;
  let ans = 0;
  const memo = new Map();

  for (let i = start; i <= end; i++) {
    const sortedDigits = getSortedDigits(i);
    if (!memo.has(sortedDigits)) {
      memo.set(sortedDigits, isPalindromePermutation(i, k));
    }
    if (memo.get(sortedDigits)) {
      ans++;
    }
  }

  return ans;
}

function getSortedDigits(num) {
  return num.toString().split('').sort().join('');
}

function isPalindromePermutation(num, k) {
  const s = num.toString();
  const permutations = new Set();
  generatePermutations(s.split(''), 0, permutations);

  for (const perm of permutations) {
    if (perm[0] === '0') continue;
    if (isPalindrome(perm) && parseInt(perm) % k === 0) {
      return true;
    }
  }

  return false;
}

function generatePermutations(arr, index, result) {
  if (index === arr.length - 1) {
    result.add(arr.join(''));
    return;
  }

  for (let i = index; i < arr.length; i++) {
    [arr[index], arr[i]] = [arr[i], arr[index]];
    generatePermutations(arr, index + 1, result);
    [arr[index], arr[i]] = [arr[i], arr[index]]; // backtrack
  }
}

function isPalindrome(s) {
  let i = 0, j = s.length - 1;
  while (i < j) {
    if (s[i++] !== s[j--]) return false;
  }
  return true;
}