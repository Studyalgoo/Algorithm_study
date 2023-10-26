n, m = map(int, input().split())

# 빈 2차원 배열 생성
relations = [ [] for _ in range(n) ]

visited = [False] * 2001
isFinish = False

# 친구관계 입력받기
for i in range(m):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

def dfs(index, depth):
    global isFinish

    visited[index] = True

    if depth == 4:
        isFinish = True
        return
    
    for i in relations[index]:
        if visited[i] == False:
            dfs(i , depth+1)
    visited[index] = False

# 사람 수만큼 dfs 진행
for i in range(n):
    dfs(i, 0)

    if isFinish:
        break

if isFinish:
    print(1)
else:
    print(0)