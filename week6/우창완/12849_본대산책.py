from collections import deque

d = int(input())


def solution():
    dp = list(list([0] * (d + 1) for _ in range(3)) for _ in range(3))
    dp[1][0][1] = 1
    dp[2][0][2] = 2
    dp[0][1][1] = 1
    rest = 1000000007

    queue = deque()
    queue.append((0, 0, 0))

    while queue:
        x, y, cnt = queue.popleft()

        if cnt >= d:
            continue

        if x == 1 and y == 1:
            dp[2][0][cnt + 1] = (dp[2][0][cnt + 1] + dp[1][1][cnt]) % rest
            queue.append((2, 0, cnt + 1))
        elif x == 2 and y == 0:
            dp[1][1][cnt + 1] += (dp[1][1][cnt + 1] + dp[2][0][cnt]) % rest
            queue.append((1, 1, cnt + 1))
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx = x + dx
            ny = y + dy
            if nx == 0 and ny == 2:
                continue

            if 0 <= nx < 3 and 0 <= ny < 3:
                dp[nx][ny][cnt + 1] = (dp[nx][ny][cnt + 1] + dp[x][y][cnt]) % rest
                queue.append((nx, ny, cnt + 1))
    print(dp[0][0])


solution()
