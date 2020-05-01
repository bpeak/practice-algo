const maxAndMin = (arr1, arr2) => {
  arr1.sort((a, b) => a - b)
  arr2.sort((a, b) => a - b)
  const max1 = arr1[arr1.length - 1]
  const min1 = arr1[0]
  const max2 = arr2[arr2.length - 1]
  const min2 = arr2[0]
  const maxDiff = Math.max(Math.abs(max1 - min2), Math.abs(max2 - min1))
  return maxDiff
}
console.log(maxAndMin([3,10,5],[20,7,15,8]))
// const maxAndMin = (arr1, arr2) => {
//   let max = -1
//   let min = Infinity
//   arr1.forEach(v1 => {
//     arr2.forEach(v2 => {
//       const diff = Math.abs(v1 - v2)
//       if(diff > max){ max = diff }
//       if(diff < min){ min = diff }
//     })
//   })
//   return [max, min]
// }
// console.log(maxAndMin([3,10,5],[20,7,15,8]))
// const maxOfArr = (arr) => Math.max.apply(null, arr)
// const minOfArr = (arr) => Math.min.apply(null, arr)
// const abs = (num) => Math.abs(num)
// const maxAndMin = (arr1, arr2) => {
//   const max1 = maxOfArr(arr1)
//   const min1 = minOfArr(arr1)
//   const max2 = maxOfArr(arr2)
//   const min2 = minOfArr(arr2)
//   const maxDiff = maxOfArr([abs(max1 - min2), abs(max2 - min1)])
//   const minDiff = minOfArr([abs(min1 - min2), abs(max1 - max2)])
//   console.log(maxDiff, minDiff)
// }
// maxAndMin([3,10,5],[20,7,15,8])