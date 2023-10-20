from collections import deque

# w: 다리의 길이, l: 다리의 최대하중
n, w, l = list(map(int, input().split()))
trucks = deque(map(int, input().split()))

time = 0

queue = deque()
queue.append((w, trucks.popleft()))
total_weight = queue[0][1]

while trucks:
    next_queue = deque()
    time += 1

    for item in list(queue):
        left, weight = queue.popleft()
        if left - 1 != 0:
            next_queue.append((left - 1, weight))
        else:
            total_weight -= weight

    if total_weight + trucks[0] <= l:
        truck_weight = trucks.popleft()
        next_queue.append((w, truck_weight))
        total_weight += truck_weight

    queue = next_queue


print(time + w + 1)
