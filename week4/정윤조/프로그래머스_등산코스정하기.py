import sys,heapq
INF=sys.maxsize
from collections import defaultdict

def solution(n, paths, gates, summits):
    summits=set(summits)
    gates=set(gates)
    graph=defaultdict(set)
    for i,j,w in paths:
        graph[i].add((j,w))
        graph[j].add((i,w))
    
    pq=[]
    heapq.heapify(pq)
    intensities=[INF]*(n+1)
    for gate in gates:
        intensities[gate]=0
        heapq.heappush(pq,(0,gate))
    
    while pq:
        intensity1,node=heapq.heappop(pq)
        if intensities[node]<intensity1 or node in summits:
            continue            
        
        for neighbor,intensity2 in graph[node]:
            nextIntensity=max(intensity1,intensity2)
            if intensities[neighbor]>nextIntensity:
                intensities[neighbor]=nextIntensity
                heapq.heappush(pq,(nextIntensity,neighbor))
    
    answer=[-1,INF]
    for summit in sorted(summits):
        if intensities[summit]<answer[1]:
            answer[0]=summit
            answer[1]=intensities[summit]
    
    return answer