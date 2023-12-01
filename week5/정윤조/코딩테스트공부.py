import sys
INF=sys.maxsize
def solution(alp, cop, problems):
    target_alp=0
    target_cop=0
    for alp_req,cop_req,alp_rwd,cop_rwd,cost in problems:
        target_alp=max(alp_req,target_alp)
        target_cop=max(cop_req,target_cop)
    dp=[[INF]*(target_cop+1) for _ in range(target_alp+1)]
    alp=min(target_alp,alp)
    cop=min(target_cop,cop)
    dp[alp][cop]=0
    for i in range(alp,target_alp+1):
        for j in range(cop,target_cop+1):
            if i<target_alp:
                dp[i+1][j]=min(dp[i+1][j],dp[i][j]+1)
            if j<target_cop:
                dp[i][j+1]=min(dp[i][j+1],dp[i][j]+1)
            for alp_req,cop_req,alp_rwd,cop_rwd,cost in problems:
                if i>=alp_req and j>=cop_req:
                    next_alp=min(i+alp_rwd,target_alp)
                    next_cop=min(j+cop_rwd,target_cop)
                    dp[next_alp][next_cop]=min(dp[next_alp][next_cop],dp[i][j]+cost)
         
    return dp[target_alp][target_cop]