const maxAndMin = (arr1, arr2) => {
  arr1.sort((a, b) => a - b) // nlogn
  arr2.sort((a, b) => a - b) // nlogn
  const max1 = arr1[arr1.length - 1]
  const min1 = arr1[0]
  const max2 = arr2[arr2.length - 1]
  const min2 = arr2[0]

  const maxDiff = Math.max(Math.abs(max1 - min2), Math.abs(max2 - min1)) // n

  arr1 = arr1.map((v) => ({ own:1, v })) // nlogn
  arr2 = arr2.map((v) => ({ own:2, v })) // nlogn
  const arr = arr1.concat(arr2)
  arr.sort((a, b) => a.v - b.v) // nlogn

  let minDiff = Infinity
  for(let i = 0; i < arr.length - 1; i++) { // n
    if(arr[i].own === arr[i + 1].own){ continue }
    const currDiff = Math.abs(arr[i].v - arr[i + 1].v)
    if(currDiff < minDiff) { minDiff = currDiff }
  }

  // total: nlogn
  return [maxDiff, minDiff]
}
console.log(maxAndMin([3,10,5],[20,7,15,8]))


// const maxAndMin_fail = (arr1, arr2) => {
//   let max = -1
//   let min = Infinity
//   // n^2
//   arr1.forEach(v1 => {
//     arr2.forEach(v2 => {
//       const diff = Math.abs(v1 - v2)
//       if(diff > max){ max = diff }
//       if(diff < min){ min = diff }
//     })
//   })
//   return [max, min]
// }

// console.log(maxAndMin_fail([3,10,5],[20,7,15,8]))