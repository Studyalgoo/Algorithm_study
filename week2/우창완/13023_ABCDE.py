import sys

n, m = list(map(int, input().split()))
arr = list(list(map(int, input().split())) for _ in range(m))
graph = [[] for _ in range(n)]

for start, end in arr:
    graph[start].append(end)
    graph[end].append(start)


def dfs(x, depth):
    if depth == 5:
        return True

    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            if dfs(nx, depth + 1):
                return True
            visited[nx] = False

    return False


for i in range(n):
    visited = [False] * n
    visited[i] = True
    if dfs(i, 1):
        print(1)
        sys.exit()

print(0)
