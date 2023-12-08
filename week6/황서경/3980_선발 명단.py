import sys

input = sys.stdin.readline

def solution(cnt, summ):
    global result

    # 종료
    if cnt == 11:
        result = max(result, summ)
        return
    
    for i in range(11):
        # 이미 포지션이 정해졌거나 해당 포지션 능력치가 0인 경우
        if visited[i] or not skills[cnt][i]:
            continue

        # 능력치가 0이 아니면
        visited[i] = 1
           
        solution(cnt+1, summ + skills[cnt][i])
            
        visited[i] = 0

for _ in range(int(input())):

    skills = [list(map(int, input().split())) for _ in range(11)]

    result = 0
    #선수가 포지션에 있는지
    visited = [0 for _ in range(11)]

    solution(0, 0)
    print(result)