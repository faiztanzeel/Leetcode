/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
   const string1= s.toLowerCase().replace(/[^a-z0-9]/g,'');
   const string2=string1.split('').reverse().join('');
   return string1===string2;
};