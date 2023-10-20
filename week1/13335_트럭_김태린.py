const fs = require('fs')

let a = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
let [trucks_cnt, bridge_length, weight] = a[0].split(' ').map(Number)
let trucks = a[1].split(' ').map(Number)

let cnt = 0
//다리 상태를  que의 형태로 표현
let que = new Array(bridge_length).fill(0);

while(que.length) {
  que.shift()

  if (trucks.length) {
    //다리 위 무게 상태
    let sum = que.reduce((a,b) => a+b)

    if(weight >= sum + trucks[0]) {
      let a = trucks.shift()
      que.push(a)

    }else {
      que.push(0)

    }
  }
  cnt += 1

}

console.log(cnt)