var kidsWithCandies = function(candies, extraCandies) {
  const max = Math.max.apply(null, candies)
  return candies.map(candy => ((candy + extraCandies) >= max) ? true : false)
};
console.log(kidsWithCandies([2,3,5,1,3], 3))