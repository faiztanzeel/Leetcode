/**
 * @param {number[]} arr
 * @return {boolean}
 */
function threeConsecutiveOdds(arr) {
  let count = 0;
  for (const num of arr) {
    if (num % 2 !== 0) {
      count++;
      if (count === 3) {
        return true;
      }
    } else {
      count = 0;
    }
  }
  return false;
}