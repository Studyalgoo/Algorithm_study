import sys

input = sys.stdin.readline


def solve(y, total):
    global answer, visited
    if y == 11:
        answer = max(answer, total)
        return

    for x in range(11):
        if visited[x]:
            continue
        if squad[y][x] == 0:
            continue
        total += squad[y][x]
        visited[x] = True
        solve(y + 1, total)
        total -= squad[y][x]
        visited[x] = False


test_case = int(input())
for _ in range(test_case):
    squad = [list(map(int, input().split())) for _ in range(11)]
    visited = [False] * 11
    answer = 0

    solve(0, 0)
    print(answer)
