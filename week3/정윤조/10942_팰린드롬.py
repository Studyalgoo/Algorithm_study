import sys
input=sys.stdin.readline

N=int(input())# 1<=N<=2000
arr=[0]+list(map(int,input().split()))
M=int(input())# 1<=M<=1000000

"""
시간초과
def isPalindrome(s,e):
    if s==e:
        return 1
    
    mid=(s+e)//2
    num=mid-s

    if (s+e)%2==1:
        for j in range(num+1):
            if arr[mid-j]!=arr[mid+1+j]:
                return 0
        return 1

    for i in range(1,num+1):
        if arr[mid-i]!=arr[mid+i]:
            return 0
            
    return 1   시간복잡도: N/2*M 대략 10억            
             


for i in range(M):
    start,end=map(int,input().split())
    print(isPalindrome(start,end))
"""

dp=[[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1): # 길이가 1
    dp[i][i]=1

for i in range(1,N):   # 길이가 2
    if arr[i]==arr[i+1]:
        dp[i][i+1]=1
    

for l in range(2,N): #길이가 3이상
    for i in range(1,N-(l-1)):
        if arr[i]==arr[i+l] and dp[i+1][i+l-1]:
            dp[i][i+l]=1
       
    
for i in range(M):
    start,end=map(int,input().split())
    print(dp[start][end]) #시간:2152ms