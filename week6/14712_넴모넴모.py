import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (m + 1) for _ in range(n + 1)]
result = 0

# 2*2 중 하나라도 넴모가 없을 때만 (x,y)에 넣기
# (1, 1) -> (m, n)
def dfs(x, y):
    global result

    # 탐색 완료
    if (x, y) == (1, n+1):
        result += 1
        return
    
    # 현재 위치가 마지막 행이면
    if x == m:
        nx, ny = 1, y+1
    else:
        nx, ny = x+1, y
    
    # 넴모를 놓지 않는 경우
    dfs(nx, ny)

    # 넴모를 놓는 경우 (좌측, 상단, 좌상단에 넴모가 없는지 체크)
    if graph[y - 1][x] == 0 or graph[y-1][x - 1] == 0 or graph[y][x - 1] == 0: 
        graph[y][x] = 1
        dfs(nx, ny)
        # 다시 되돌아오면 0
        graph[y][x] = 0
        
        
dfs(1, 1)
print(result)