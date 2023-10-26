import heapq, sys
from collections import deque

input = sys.stdin.readline

n = int(input())
courses = deque(list(map(int, input().split())) for _ in range(n))
courses = deque(sorted(courses, key=lambda x: x[0]))

count = 0
heap = []
start, end = courses.popleft()
heapq.heappush(heap, [end, start])

for i in range(len(courses)):
    start, end = courses.popleft()
    # 끝나는 시간이 시작시간과 빠르거나 같다면
    while heap and heap[0][0] <= start:
        heapq.heappop(heap)

    heapq.heappush(heap, [end, start])
    count = max(count, len(heap))

print(count)
