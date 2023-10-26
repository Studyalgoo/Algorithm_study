import sys

n = int(sys.stdin.readline())

route = []
for i in range(n):
    route.append(input().split())

# 오른쪽, 아래 방향만 갈 수 있음
dx = [1, 0]
dy = [0, 1]

# 최소, 최대 설정
MIN = int(1e9)
MAX = -int(1e9)

def getAnswer(x, y, p, oper):
    global MIN, MAX

    for i in range(2):
        ax = x + dx[i]
        ay = y + dy[i]

        if (0 <= ax < n) and (0 <= ay < n):
            # 연산자 나올 경우 재귀 돌림
            if route[ax][ay] == '-':
                getAnswer(ax, ay, p, '-')
            elif route[ax][ay] == '+':
                getAnswer(ax, ay, p, '+')
            elif route[ax][ay] == '*':
                getAnswer(ax, ay, p, '*')
            # 재귀 돌린 후 계산
            else:
                if oper == '+': 
                    result = p + int(route[ax][ay])
                elif oper == '-': 
                    result = p - int(route[ax][ay])
                elif oper == '*': 
                    result = p * int(route[ax][ay])
                # 계산 다 끝나면 최대, 최소 구함
                if ax == n-1 and ay == n-1:
                    MIN = min(MIN, result)
                    MAX = max(MAX, result)
                    return
                # 계산 다 안 끝나면 다시 재귀 
                getAnswer(ax, ay, result, '')

getAnswer(0, 0, int(route[0][0]), '')
print(MAX, MIN)

