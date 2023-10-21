const fs = require('fs')

let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
let num = input[3]

//a그룹
let a = input[1].split('').reverse().join('')

let b = input[2].split('').join('')

let list = (a + b).split('')


for(let i=0; i<num; i++) {
  for(let j=0; j<list.length; j++) {
    if(a.includes(list[j]) && b.includes(list[j+1])) {
      let temp = list[j]
      list[j] = list[j+1]
      list[j+1] = temp

      //반복문 멈추기
      if(list[j+1] === a[a.length-1]) {
        break
      }
    }
  }
}

console.log(list.join(''))