const solution = (offers) => {
	class Offer {
		constructor(offerStr) {
			const [startDateStr, endDateStr, salaryStr] = offerStr.split(" ");
      this.salary = Number(salaryStr)
      this.startTimestamp = this._parseTimestampFromDateStr(startDateStr)
      this.endTimestamp = this._parseTimestampFromDateStr(endDateStr)
		}
		_parseTimestampFromDateStr = (dateStr) => {
      const [ monthStr, dayStr ] = dateStr.split("/")
      return Number(new Date(2020, monthStr, dayStr))
		}
  }
	
	// start offer
	let currOfferIdx = 0
  let currOffer = new Offer(offers[0])
  offers.some((offerStr, candiOfferIdx) => {
    const candiOffer = new Offer(offerStr)
    if(currOffer.startTimestamp !== candiOffer.startTimestamp) { return }
    if(candiOffer >= currOffer) {
      currOffer = candiOffer
      currOfferIdx = candiOfferIdx
    }
  })

	// find offer
  for(let i = currOfferIdx + 1; i < offers.length; i++) {
    const candiOffer = new Offer(offers[i])
    if(currOffer.endTimestamp < candiOffer.startTimestamp) {
      return currOffer.salary
    }
    if(
      (candiOffer.salary > currOffer.salary) ||
      (candiOffer.salary === currOffer.salary && candiOffer.endTimestamp >= currOffer.endTimestamp)
    ) {
      currOffer = candiOffer
    }
  }
}

console.log(solution(["10/05 10/12 2400", "10/05 10/10 2500", "10/07 10/15 2300", "10/08 10/30 3000", "10/15 11/03 3000", "10/20 11/01 3500", "11/02 11/11 4000"])) // 3500
console.log(solution(["07/01 07/30 2000", "07/01 07/15 2000", "07/01 07/30 2000", "07/01 07/30 1500", "07/05 07/30 2100", "07/20 08/01 2400", "07/20 07/31 2400", "07/31 09/01 2900", "08/01 08/15 3000", "08/14 08/19 2000","08/17 08/30 4000"])) // 3000