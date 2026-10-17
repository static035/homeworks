// function addBinary(a,b) {
//   const total = a+b
//   return total.toString("2")
// }

// // TEST CASES
// console.log(addBinary(0,1))
// console.log(addBinary(1,0))
// console.log(addBinary(2,2))
// console.log(addBinary(51,12))

// function validatePIN (pin) {
//   if (!/^(\d{4}|\d{6})$/gi.test(pin)) {
//     return false
//   }
//   if (pin.length === 4 || pin.length === 6) {
//     return true
//   }
//   return false
// }

// // TEST CASES
// console.log(validate_pin("1"))
// console.log(validate_pin("12"))
// console.log(validate_pin("123"))
// console.log(validate_pin("12345"))
// console.log(validate_pin("1234567"))
// console.log(validate_pin("-123434'"))
// console.log(validate_pin("-12345345"))
// console.log(validate_pin("1.234"))
// console.log(validate_pin("00000000"))

// function binaryArrayToNumber(arr) {
//     let stringifiedArr = []
//     for (let i = 0; i < arr.length; i++) {
//         stringifiedArr.push(String(arr[i]))
//     }
        
//     let stringed = stringifiedArr.join("")
//     return parseInt(stringed, 2)
// }

// // TEST CASES
// console.log(binaryArrayToNumber([0,0,0,1]))
// console.log(binaryArrayToNumber([0,0,1,0]))
// console.log(binaryArrayToNumber([1,1,1,1]))
// console.log(binaryArrayToNumber([0,1,1,0]))