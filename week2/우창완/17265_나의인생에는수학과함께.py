import sys
from collections import deque

n = int(input())

graph = list(list(map(str, input().split())) for _ in range(n))
operators = ["+", "-", "*"]


def bfs(x, y):
    queue = deque()
    queue.append((x, y, "_", int(graph[x][y])))
    max_value = -sys.maxsize
    min_value = sys.maxsize

    while queue:
        x, y, operator, path_value = queue.popleft()

        if x == n - 1 and y == n - 1:
            max_value = max(max_value, path_value)
            min_value = min(min_value, path_value)

        for dx, dy in (1, 0), (0, 1):
            nx = dx + x
            ny = dy + y
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            # 연산자 칸 일 경우
            if graph[nx][ny] in operators:
                queue.append((nx, ny, graph[nx][ny], path_value))
            # 숫자칸 일 경우
            else:
                value = int(graph[nx][ny])
                if operator == "*":
                    temp = path_value * value
                elif operator == "+":
                    temp = path_value + value
                else:
                    temp = path_value - value
                queue.append((nx, ny, "_", temp))
    print(max_value, min_value)


bfs(0, 0)
