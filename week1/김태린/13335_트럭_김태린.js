const fs = require('fs');

let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let [trucks_cnt, bridge_length, weight] = input[0].split(' ').map(Number);
let trucks = input[1].split(' ').map(Number);

let cnt = 0;
let que = new Array(bridge_length).fill(0);
let totalWeight = 0;

while (que.length) {
    cnt++;

    // 큐에서 나가는 트럭의 무게를 빼줌 -> 시간 줄이기!!!
    totalWeight -= que.shift();
    
    if (trucks.length) {
        // 새로운 트럭이 다리에 올라갈 수 있는 경우
        if (totalWeight + trucks[0] <= weight) {
            let newTruck = trucks.shift();
            que.push(newTruck);
            totalWeight += newTruck;
        } else {
            // 새로운 트럭이 다리에 올라갈 수 없는 경우
            que.push(0);
        }
    }
}

console.log(cnt);