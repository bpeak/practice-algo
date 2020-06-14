const solution = (N, facilities) => {
  let minAccessCost = Infinity
  for(let x = 1; x <= N; x++) {
    for(let y = 1; y <= N; y++) {
      const accessCostCandidate = facilities.reduce((accessCostCandidate, [facility_x, facility_y, facility_importance]) => {
        const diff_x = Math.abs(facility_x - x)
        const diff_y = Math.abs(facility_y - y)
        const currAccessCost = (diff_x + diff_y) * facility_importance
        if(currAccessCost > accessCostCandidate) {
          accessCostCandidate = currAccessCost
        }   
        return accessCostCandidate
      }, -1)
      if(accessCostCandidate < minAccessCost) {
        minAccessCost = accessCostCandidate
      }
    }
  }
  return minAccessCost
}

console.log(solution(3, [[1,3,1], [3,1,1]]))
console.log(solution(3, [[1,3,2], [3,1,1]]))
console.log(solution(3, [[1,1,1]]))