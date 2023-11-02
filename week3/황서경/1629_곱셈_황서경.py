import sys

a, b, c = map(int, sys.stdin.readline().split())

# 분할 정복 함수 구현
def Recursive_Power(a, b, c):
    if b == 1:
        return a % c
    else:
        result = Recursive_Power(a, b//2, c)

        # b가 짝수일 경우 (ex: 10^4 = 10^2*10^2)
        if b % 2 == 0:
            return result*result%c
        # b가 홀수일 경우 (ex: 10^5 = 10^2*10^2*10)
        else:
            return result*result*a%c
    
print(Recursive_Power(a, b, c))
