const fs = require('fs');

let [a, b, c] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(BigInt);


//분할 정복 알고리즘 사용
const pow = (a, b, c) => {
  //b가 1이면 바로 c로 나누기
  if (b === BigInt(1)) {
    return a % c;
  }
  const halfPow = pow(a, BigInt(parseInt(b / BigInt(2))), c);

  //짝수일때 
  if (b % BigInt(2) === BigInt(0)) {
    return (halfPow * halfPow) % c;

  } 
  //홀수일때 - a를 한번 더 곱해주기 
  else {
    return ((halfPow * halfPow * a) % c);
  }
};

console.log(Number(pow(a, b, c)));