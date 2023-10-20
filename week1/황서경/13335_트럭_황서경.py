n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0] * w
time = 0

while bridge:
    time += 1
    bridge.pop(0)

    if trucks:
        if trucks[0] + sum(bridge) <= L:
            bridge.append(trucks.pop(0))
        else:
            bridge.append(0)

print(time)