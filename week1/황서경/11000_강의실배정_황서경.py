import heapq
import sys

N = int(sys.stdin.readline())

list1 = []
q = []

list1 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

list1.sort()

heapq.heappush(q, list1[0][1])  # 젤 빨리 끝나는 시간

for i in range(1, N):
    if q[0] > list1[i][0]:
        heapq.heappush(q, list1[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q, list1[i][1])

print(len(q))