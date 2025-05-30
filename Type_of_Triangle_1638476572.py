const triangleType = nums => {
  const [a, b, c] = nums;

  if (
    a + b <= c ||
    a + c <= b ||
    b + c <= a
  ) return 'none';

  if (
    a === b &&
    a === c
  ) return 'equilateral';

  if (
    a === b ||
    a === c ||
    b === c
  ) return 'isosceles';

  return 'scalene';
};