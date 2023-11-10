import sys
input=sys.stdin.readline

A,B,C=map(int,input().split())# 0<A,B,C<2147483647

def Gob(x,n,mod):
    if n==1:
        return x%mod
    
    mid=n//2
    ret=Gob(x,mid,mod)## 이 값을 메모이제이션 하는게 핵심
    
    if n%2==0:
        return (ret*ret)%mod

    return (x*ret*ret)%mod


print(Gob(A,B,C))

##시간:40ms