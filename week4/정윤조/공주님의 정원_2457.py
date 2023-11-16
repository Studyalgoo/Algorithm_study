import sys,heapq
input=sys.stdin.readline

N=int(input())# 1<=N<=100000
Months=[0,31,28,31,30,31,30,31,31,30,31,30,31]
def dateToNum(month,day):
    num=day
    for i in range(month):
        num+=Months[i]
    return num
    

date31=dateToNum(3,1)
date121=dateToNum(12,1)
dates=[]
for i in range(N):
    m1,d1,m2,d2=map(int,input().split())
    datem1d1=dateToNum(m1,d1)
    datem2d2=dateToNum(m2,d2)
    if datem1d1<date31:
        datem1d1=date31
    if datem2d2>=date121:
        datem2d2=date121
    dates.append((datem1d1,datem2d2))

dates.sort(key=lambda x:x[0])

maxHeap=[-date31]
heapq.heapify(maxHeap)

idx=0
while idx<N:
    tmp=-maxHeap[0]
    jump=idx
    if dates[idx][0]<=tmp and dates[idx][1]>tmp:
        heapq.heappush(maxHeap,-dates[idx][1])
        for j in range(idx+1,N):
            if dates[j][0]<=tmp and dates[j][1]>tmp and dates[j][1]>-maxHeap[0]:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap,-dates[j][1])
                jump=j
    idx=jump+1

if -maxHeap[0]<date121:
    print(0)
else:
    print(len(maxHeap)-1)