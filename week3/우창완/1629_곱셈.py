a, b, c = list(map(int, input().split()))


def dfs(a, b, c):
    if b == 0:
        return 1
    if b % 2 == 1:
        return (dfs(a, b // 2, c) ** 2 * a) % c
    else:
        return (dfs(a, b // 2, c) ** 2) % c


print(dfs(a, b, c))
