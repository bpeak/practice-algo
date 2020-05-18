function solution(BRIDGE_LENGTH, BRIDGE_WEIGHT, truckWeights) {
	t = 0
	trucksOnBridge = []
	while(truckWeights.length !== 0 || trucksOnBridge.length !== 0){
		trucksOnBridge = trucksOnBridge
			.map(v => ({...v, spentTime: v.spentTime + 1}))
			.filter((v) => v.spentTime < BRIDGE_LENGTH)

		const sumOfTrucksOnBridge = trucksOnBridge.reduce((acc, curr) => acc + curr.weight, 0)

		if((sumOfTrucksOnBridge + truckWeights[0]) <= BRIDGE_WEIGHT) {
			trucksOnBridge.push({
				weight: truckWeights.shift(),
				spentTime: 0,
			})
		}
		t++
	}
	return t
}

console.log(solution(2, 10, [7,4,5,6])) // 8
console.log(solution(100, 100, [10])) // 101
console.log(solution(100, 100, [10,10,10,10,10,10,10,10,10,10])) // 110