import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]

m = int(input())

for i in range(n):
    dp[i][i] = 1


def dfs(start, end):
    if start >= end:
        return True

    if dp[start][end]:
        return dp[start][end] == 1

    if arr[start] == arr[end] and dfs(start + 1, end - 1):
        dp[start][end] = 1
        return True
    dp[start][end] = -1
    return False


for i in range(m):
    s, e = list(map(int, input().split()))
    print(1 if dfs(s - 1, e - 1) else 0)
