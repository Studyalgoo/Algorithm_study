import sys

n = int(sys.stdin.readline())
flowers = []
count = 0

# 계산 편의를 위해 월에 해당하는 숫자에 100을 곱함
for _ in range(n):
    date = list(map(int, sys.stdin.readline().split()))
    flowers.append([date[0] * 100 + date[1], date[2] * 100 + date[3]])

flowers.sort()

end = 0 # 0으로 시작점 임의설정, end는 계속해서 가장 마지막으로 꽃이 지는 날로 업데이트됨
start = 301

while flowers:
    # 비교할 필요 X
    if start >= 1201 or flowers[0][0] > start:
        break

    # 비교 시작
    for _ in range(len(flowers)):
        # 배열 처음에 있는 시작 날짜가 마지막으로 꽂이 지는 날짜보다 작으면
        if flowers[0][0] <= start:
            # 해당 꽃의 지는 날짜와 마지막으로 꽃이 지는 날 비교
            if end <= flowers[0][1]:
                end = flowers[0][1]

            flowers.remove(flowers[0])

        # 꽃이 지는 날이 제일 빨리 피는 꽃보다 작으면 break
        else:
            break

    start = end
    count += 1

if start < 1201:
    print(0)
else:
    print(count)

