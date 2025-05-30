/**
 * Computes the maximum score achievable by selecting numbers based on their distinct prime factors
 * and multiplying them within a limited number of operations.
 * 
 * @param {number[]} numbers - An array of positive integers.
 * @param {number} maxOperations - The maximum number of multiplication operations allowed.
 * @returns {number} The final computed score modulo 1_000_000_007.
 */
function maximumScore(numbers, maxOperations) {
  const MODULO = 1000000007n;
  const n = numbers.length;

  // ───────────────────────────────────────────────────────────────
  // Step 1: Precompute all prime numbers up to √max(numbers[])
  // This allows efficient factorization of any number ≤ max(numbers)
  // ───────────────────────────────────────────────────────────────
  const maxValue = Math.max(...numbers);
  const sqrtLimit = Math.floor(Math.sqrt(maxValue)) + 1;
  const isPrime = new Array(sqrtLimit + 1).fill(true);
  isPrime[0] = isPrime[1] = false;
  const primes = [];

  for (let candidate = 2; candidate <= sqrtLimit; candidate++) {
    if (isPrime[candidate]) {
      primes.push(candidate);
      for (let multiple = candidate * candidate; multiple <= sqrtLimit; multiple += candidate) {
        isPrime[multiple] = false;
      }
    }
  }

  // ───────────────────────────────────────────────────────────────
  // Step 2: Count distinct prime factors using cached trial division
  // ───────────────────────────────────────────────────────────────
  const distinctPrimeFactorCache = new Map();

  /**
   * Count the number of distinct prime factors for a given number.
   * Uses precomputed primes for fast factorization.
   * 
   * @param {number} value
   * @returns {number}
   */
  function countDistinctPrimeFactors(value) {
    if (distinctPrimeFactorCache.has(value)) {
      return distinctPrimeFactorCache.get(value);
    }

    let count = 0;
    let temp = value;

    for (let i = 0, len = primes.length; i < len && primes[i] * primes[i] <= temp; i++) {
      const prime = primes[i];
      if (temp % prime === 0) {
        count++;
        while (temp % prime === 0) {
          temp = Math.floor(temp / prime);
        }
      }
    }

    // If remaining value > 1, it's a distinct prime itself
    if (temp > 1) count++;

    distinctPrimeFactorCache.set(value, count);
    return count;
  }

  // ───────────────────────────────────────────────────────────────
  // Step 3: Compute prime score (distinct prime factors) for each number
  // ───────────────────────────────────────────────────────────────
  const primeFactorCounts = new Array(n);
  for (let index = 0; index < n; index++) {
    primeFactorCounts[index] = countDistinctPrimeFactors(numbers[index]);
  }

  // ───────────────────────────────────────────────────────────────
  // Step 4: For each index, compute the subarray span where this index
  //         holds the maximum prime score (with tie-breaker: smallest index)
  // 
  // leftBoundary[i] = nearest index on the left with primeScore ≥ current
  // rightBoundary[i] = nearest index on the right with primeScore > current
  // ───────────────────────────────────────────────────────────────
  const leftBoundary = new Array(n).fill(-1);
  const rightBoundary = new Array(n).fill(n);
  const stack = [];

  // Compute left boundaries using monotonic stack (non-increasing)
  for (let index = 0; index < n; index++) {
    while (stack.length && primeFactorCounts[stack[stack.length - 1]] < primeFactorCounts[index]) {
      stack.pop();
    }
    leftBoundary[index] = stack.length ? stack[stack.length - 1] : -1;
    stack.push(index);
  }

  stack.length = 0;

  // Compute right boundaries using monotonic stack (strictly decreasing)
  for (let index = n - 1; index >= 0; index--) {
    while (stack.length && primeFactorCounts[stack[stack.length - 1]] <= primeFactorCounts[index]) {
      stack.pop();
    }
    rightBoundary[index] = stack.length ? stack[stack.length - 1] : n;
    stack.push(index);
  }

  // ───────────────────────────────────────────────────────────────
  // Step 5: Calculate frequency (i.e. number of subarrays where
  //         numbers[i] would be chosen as the max prime score element)
  // 
  // Frequency = (# options on left) × (# options on right)
  //            = (i - left[i]) * (right[i] - i)
  //
  // Then aggregate all contributions for each unique number.
  // ───────────────────────────────────────────────────────────────
  const maxOperationsBigInt = BigInt(maxOperations);
  const frequencyByNumber = new Map();

  for (let index = 0; index < n; index++) {
    const leftOptions = BigInt(index - leftBoundary[index]);
    const rightOptions = BigInt(rightBoundary[index] - index);
    const frequency = leftOptions * rightOptions;
    const capped = frequency > maxOperationsBigInt ? maxOperationsBigInt : frequency;

    frequencyByNumber.set(
      numbers[index],
      (frequencyByNumber.get(numbers[index]) || 0n) + capped
    );
  }

  // ───────────────────────────────────────────────────────────────
  // Step 6: Sort numbers in descending order and greedily use the best
  //         multipliers first until operations run out
  // ───────────────────────────────────────────────────────────────
  const aggregatedEntries = Array.from(frequencyByNumber.entries());
  aggregatedEntries.sort((a, b) => b[0] - a[0]); // Sort by number (not frequency)

  /**
   * Compute (base ^ exponent) % modulus efficiently using binary exponentiation.
   * 
   * @param {bigint} base 
   * @param {bigint} exponent 
   * @param {bigint} modulus 
   * @returns {bigint}
   */
  function modPow(base, exponent, modulus) {
    let result = 1n;
    base %= modulus;
    while (exponent > 0n) {
      if (exponent & 1n) {
        result = (result * base) % modulus;
      }
      base = (base * base) % modulus;
      exponent >>= 1n;
    }
    return result;
  }

  // ───────────────────────────────────────────────────────────────
  // Step 7: Apply the selected multipliers and return final score
  // ───────────────────────────────────────────────────────────────
  let finalScore = 1n;
  let remainingOperations = maxOperationsBigInt;

  for (const [numberValue, totalFrequency] of aggregatedEntries) {
    if (remainingOperations === 0n) break;
    const uses = totalFrequency < remainingOperations ? totalFrequency : remainingOperations;
    finalScore = (finalScore * modPow(BigInt(numberValue), uses, MODULO)) % MODULO;
    remainingOperations -= uses;
  }

  return Number(finalScore);
}