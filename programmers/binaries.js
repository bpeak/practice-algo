function code (string) {
  const result = string.split("").map((char) => {
    const digitString = Number(char).toString(2)
    const zeroFill = "0".repeat(digitString.length - 1)
    return zeroFill + '1' + digitString
  }).join("")
  return result
}

function decode (string) {
  let zeroFillCount = 0
  let readFlag = false
  let digitString = ""
  let digitStrings = []
  for(let i = 0; i < string.length; i++) {
    if(readFlag) {
      zeroFillCount--
      digitString += string[i]
      if(zeroFillCount == 0) {
        readFlag = false
        digitStrings.push(digitString)
        digitString = ""
      }
    } else {
      zeroFillCount++
      if(string[i] === '1') {
        readFlag = true
      }
    }
  }
  const result = digitStrings.map(digitString => parseInt(digitString, 2)).join("")
  return result
}