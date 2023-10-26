const fs = require('fs');

let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(item => item.split(' '));
input.shift()

// dx - 오른쪽, dy - 아래로 이동
let dx = [0, 1];
let dy = [1, 0];

const n = input.length;
const m = input[0].length;

// x좌표, y좌표, 합계, 연산자의 유무
function DFS(x, y, total, oper){
  //학교에 도착할 경우
  if(x==n-1 && y==m-1) {
    //eval -> 문자열을 계산해줌
    let result = eval(total)
    minNum = Math.min(result, minNum)
    maxNum = Math.max(result, maxNum)
    return
  }else {
    //오른쪽, 아래로 이동
    for(let i=0; i<2; i++) {
      let nx = x+dx[i]
      let ny = y+dy[i]
      if(nx < n && ny < m) {
        //1. 연산자가 올 경우
        if(oper) {
          DFS(nx, ny, total+input[nx][ny], false)
        }
        //2. 숫자가 올 경우
        else{
          DFS(nx, ny, `(${total}${input[nx][ny]})`, true)
        }
      }
    }
  }
}

// x좌표, y좌표, 합계, 연산자의 유무

let minNum = Infinity;
let maxNum = -Infinity;

//깊이 우선 탐색 사용
DFS(0, 0, input[0][0], true);

console.log(maxNum, minNum);

