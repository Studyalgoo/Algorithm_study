N1, N2 = map(int, input().split())
N1_order = list(input())
N2_order = list(input())
T = int(input())

# 첫 번째 그룹 개미들 reverse
N1_order_reverse = list(reversed(N1_order))

# 합친 개미 그룹
# ['C', 'B', 'A', 'D', 'E', 'F']
new_ants = N1_order_reverse + N2_order

for _ in range(T):
    for i in range(len(new_ants)-1):
        # 서로 다른 그룹의 개미가 만나면 위치 바꾸기
        if new_ants[i] in N1_order and new_ants[i+1] in N2_order:
            new_ants[i], new_ants[i+1] = new_ants[i+1], new_ants[i]

            # 반복문 빠져나오는 조건 필요
            if new_ants[i+1] == N1_order_reverse[-1]:
                break
        
answer = ''.join(new_ants)
print(answer)

# T=1일때 -> # ['C', 'B', 'D', 'A', 'E', 'F']
# T=2일때 -> # ['C', 'D', 'B', 'E', 'A', 'F']