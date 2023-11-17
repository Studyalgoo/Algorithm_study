import sys
input=sys.stdin.readline
s1='a'+input().rstrip('\n')
s2='b'+input().rstrip('\n')

def CS(sx,sy):
    l1=len(sx)
    l2=len(sy)

    dp=[[0]*(l2) for _ in range(l1)]
    ans=0
    for i in range(1,l1):
        for j in range(1,l2):
            if sx[i]==sy[j]:
                dp[i][j]=dp[i-1][j-1]+1
                ans=max(ans,dp[i][j])
              

    return ans

print(CS(s1,s2))