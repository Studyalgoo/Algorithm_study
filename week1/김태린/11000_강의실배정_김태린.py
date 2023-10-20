const fs = require('fs')

let a = fs.readFileSync('input.txt').toString().trim().split('\n')
let list = []
let cnt = 0;

for(let i=1; i<=a[0]; i++) {
  let [b, c] = a[i].split(' ').map(Number)
  list.push([b,c])
}

list.sort((a,b) => a[0] - b[0])

let answer = [];

for(let i=0; i<=list.length; i++) {
  answer.push(list[0])
  list.shift()  
  for(let j=0; j<list.length; j++) {
    let cnt =0
    if(list[j][0] >= answer[answer.length-1][1]) {
      cnt += 1
      if(cnt == 1) {
        answer.push(list[j])
        list.splice(j, 1)
      }
    }
  }
  answer.push('구분')
}

let d= 0
for(let i=0; i<answer.length; i++) {
  if(answer[i] == '구분') {
    d+= 1
  }
}

console.log(d)