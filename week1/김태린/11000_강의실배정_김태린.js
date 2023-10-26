const fs = require('fs')

let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

let list = []

for(let i=1; i<=input[0]; i++) {
  let [b, c] = input[i].split(' ').map(Number)
  list.push([b,c])
}

//강의 시간으로 정렬
list.sort((a,b) => a[0] - b[0])

let answer = [];

//가장 첫번째 수업의 종료 시간
answer.push(list[0][1])


for(let i=1; i<list.length; i++) {
  //종료시간이 시작시간보다 크면 배열에 넣기
  if(answer[0] > list[i][0]) {
    answer.push(list[i][1])
  }else {
    answer.shift()
    answer.push(list[i][1])
  }
  answer.sort((a,b) => a-b)
}

console.log(answer.length)