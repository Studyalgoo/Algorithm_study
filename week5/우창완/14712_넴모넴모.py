import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def solution(n, m):
    graph = list(list([0] * (m + 1) for _ in range(n + 1)))
    visited = {}
    answer = 0

    def hasSquare():
        for i in range(n):
            for j in range(m):
                if graph[i][j] and graph[i + 1][j] and graph[i][j + 1] and graph[i + 1][j + 1]:
                    return True
        return False

    def backtracking(path):
        nonlocal answer, graph
        if path != '':
            print(path)
            path.sort()
        path_key = ''.join(path)

        if path_key in visited:
            return

        if hasSquare():
            return

        visited[path_key] = True
        for i in range(n):
            for j in range(m):
                if graph[i][j]:
                    continue
                answer += 1
                graph[i][j] = 1
                backtracking(path + [str(i * m + j)])
                graph[i][j] = 0

    ''.join(list([str(0)]))
    visited[''.join(list([str(0)]))] = True
    backtracking('0')
    print(visited)
    return answer


print(solution(2, 2))
# print(solution(2, 3))
# print(solution(3, 5))
n, m = list(map(int, input().split()))
print(solution(n, m))
