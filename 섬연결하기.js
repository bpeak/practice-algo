function isAllLinked(graph) {
  const firstNode = graph.keys().next().value
  if(firstNode === undefined){ return false }

  const que = [firstNode]
  const visitedNode = new Set()

  while(que.length !== 0){
    const currNode = que.pop()
    visitedNode.add(currNode)
    graph.get(currNode).forEach((adjNode) => {
      if(!visitedNode.has(adjNode)) {
        que.push(adjNode)
      }
    })
  }

  return visitedNode.size === graph.size

}

const solution = (nodeCount, nodeCosts) => {
  const costs = new Set(nodeCosts)
  const graph = new Map()
  for(let i = 0; i < nodeCount; i++) {
    graph.set(i, [])
  }

  let totalPrice = 0

  while(!isAllLinked(graph)){
    let minCost = null
    let minPrice = Infinity
    costs.forEach(currCost => {
      const [currSrc, currDst, currPrice] = currCost
      if(currPrice < minPrice) {
        minPrice = currPrice
        minCost = currCost
      }
    })

    totalPrice += minPrice
    const [src, dst] = minCost
    graph.get(src).push(dst)
    costs.delete(minCost)
  }
  
  return totalPrice

}

console.log(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))




// const solution2 = (nodeCount, nodeCosts) => {
//   const costs = new Set(nodeCosts)
//   const linkedNodes = new Set();
//   let totalPrice = 0

//   while(linkedNodes.size !== nodeCount) {
//     let minPrice = Infinity
//     let minCost = null
//     costs.forEach(currCost => {
//       const [src, dst, price] = currCost
//       if(
//         price < minPrice && 
//         (!linkedNodes.has(src) || !linkedNodes.has(dst))
//       ) {

//         minPrice = price
//         minCost = currCost
//       }
//     })

//     const [src, dst, price] = minCost
//     totalPrice += price
//     linkedNodes.add(src)
//     linkedNodes.add(dst)
//     costs.delete(minCost)
//   }
  
//   return totalPrice

// }

// console.log(solution2(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))