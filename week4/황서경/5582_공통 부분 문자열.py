import sys

input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()
result = 0

# dp 풀이 위한 배열 생성
dp = [[0] * (len(str2)+1) for _ in range(len(str1)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        # 두 개의 문자가 같으면
        if str1[i-1] == str2[j-1]:
            # 바로 직전 공통 부분 문자열의 dp 값에 1 더하기 (이런식으로 공통 부분 문자열이 점점 길어짐)
            dp[i][j] = dp[i-1][j-1] + 1
            result = max(dp[i][j], result)

print(result)
