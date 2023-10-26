n, m = list(map(int, input().split()))

n1 = str(input())
n2 = str(input())
t = int(input())

n1 = n1[::-1]

merged_ant = list(n1 + n2)
answer = ""

for i in range(t):
    for j in range(1, len(merged_ant)):
        # print(j)
        if merged_ant[j] in n2 and merged_ant[j - 1] in n1:
            # swap j, j-1
            temp = merged_ant[j]
            merged_ant[j] = merged_ant[j - 1]
            merged_ant[j - 1] = temp

            if merged_ant[j] == n1[-1]:
                break
print("".join(merged_ant))
