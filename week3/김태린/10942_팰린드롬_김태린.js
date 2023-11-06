// 시간 초과 ㅠ

// [
//   [1, 0, 1, 0, 0, 0, 1],
//   [0, 1, 0, 0, 0, 1, 0],
//   [0, 0, 1, 0, 1, 0, 0],
//   [0, 0, 0, 1, 0, 0, 0],
//   [0, 0, 0, 0, 1, 0, 1],
//   [0, 0, 0, 0, 0, 1, 0],
//   [0, 0, 0, 0, 0, 0, 1]
// ]

const fs = require('fs');

let input = fs.readFileSync('/dev/stdin').toString().split('\n');
const n = input[0]
const list = input[1].split(' ').join('')

//알고리즘 - dp 다이나믹 프로그래밍
//2차원 배열 생성
let dp = Array.from({ length: n }, () => Array.from({ length: n }, () => 0));

for(let i=0; i<n; i++) {
  //시작위치, 끝위치 같으면 -> 팰린드롬 
  dp[i][i] = 1
}

//길이가 2이상일 경우
for(let len=2; len<=n; len++) {
  for(let start=0; start<=n-len; start++) {
    let end = start + len - 1;
    //시작과 끝의 값이 일치하고 그 안에 있는 숫자가 팰린드롬이면 dp -> 1
    if(list[start] == list[end] && dp[start + 1][end - 1] == 1) {
      dp[start][end] = 1
    }
  }
}


for(let i=3; i<input.length; i++) {
  const [start, end] = input[i].split(' ').map(Number)
  console.log(dp[start-1][end-1])
}
