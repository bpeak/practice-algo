const reqTimes = [
	21,
	1,
	1,
	1,
	1,
	2,
	2,
	2,
	3,
	3,
	3,
	4,
	4,
	4,
	5,
	5,
	5,
	6,
	6,
	6,
	7,
	7,
]

function droppedRequest(reqTimes) {
	reqTimes.sort((a, b) => a - b)
	// 1초당 요청 < 3
	const sec1_map = {} 
	const sec1_survivor = [] 
	const sec1_limit = 3
	// 10초당 요청 < 20
	const sec10_map = {}
	const sec10_survivor = []
	const sec10_limit = 20
	// 60초당 요청 < 60
	const sec60_map = {}
	const sec60_survivor = []
	const sec60_limit = 60

	let droppedCount = 0

	// 1
	for(let i = 0; i < reqTimes.length; i++) {
		if(sec1_map[reqTimes[i]]) {
			sec1_map[reqTimes[i]] += 1
			if(sec1_map[reqTimes[i]] > sec1_limit) {
				continue
			}
		} else {
			sec1_map[reqTimes[i]] = 1
		}
		sec1_survivor.push(reqTimes[i])
	}
	// 10
	for(let i = 0; i < sec1_survivor.length; i++) {
		const section = Math.floor(sec1_survivor[i] / 10) * 10
		if(sec10_map[section]) {
			sec10_map[section] += 1
			if(sec10_map[section] > sec10_limit) {
				continue
			}
		} else {
			sec10_map[section] = 1
		}
		sec10_survivor.push(sec1_survivor[i])
	}

	// 60
	for(let i = 0; i < sec10_survivor.length; i++) {
		const section = Math.floor(sec10_survivor[i] / 60) * 60
		if(sec60_map[section]) {
			sec60_map[section] += 1
			if(sec60_map[section] > sec60_limit) {
				continue
			}
		} else {
			sec60_map[section] = 1
		}
		sec60_survivor.push(sec10_survivor[i])
	}

	return reqTimes.length - sec60_survivor.length
}
  
console.log(droppedRequest(reqTimes))