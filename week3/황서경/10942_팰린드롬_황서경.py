import sys

n = int(sys.stdin.readline())
boards = list(map(int, input().split()))
m = int(sys.stdin.readline())

# dp 풀이 위한 배열 생성
dp = [[0] * n for _ in range(n)]

for i in range(n):
    for s in range(n - i):
        e = s + i

        # 시작 인덱스, 끝 인덱스가 같으면 무조건 팰린드롬
        if s == e:
            dp[s][e] = 1
        # 시작, 끝 위치의 숫자가 같으면 
        elif boards[s] == boards[e]:
            # 총 세 자리 숫자이면 무조건 팰린드롬
            if s+1 == e:
                dp[s][e] = 1
            # 나머지 가운데 위치의 숫자 같은지 확인
            elif dp[s+1][e-1] == 1:
                dp[s][e] = 1
        
for k in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s-1][e-1])


    

    

