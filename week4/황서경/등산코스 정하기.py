# 편도라고 생각
# n: 지점 수, paths: 등산로, gates: 출입구, summits: 산봉우리
# 다익스트라
import heapq

def solution(n, paths, gates, summits):
    hiking = [[] for _ in range(n+1)]
    for i, j, k in paths:
        hiking[i].append([j, k])
        hiking[j].append([i, k])
    
    # 산봉우리 들렸는지 안들렸는지
    is_summit = [False] * (n+1)
    for l in summits:
        is_summit[l] = True
    
    # 출입구를 0 위치에 오도록
    visited = [10000001] * (n+1)
    queue = []
    for p in gates:
        visited[p] = 0
        heapq.heappush(queue, [0, p])
        
    while queue:
        d, i = heapq.heappop(queue)
        
        # 산봉우리는 하나만 방문하도록
        if visited[i] < d or is_summit[i]:
            continue
        for j, dd in hiking[i]:
            dd = max(visited[i], dd)
            if visited[j] > dd:
                visited[j] = dd
                heapq.heappush(queue, [dd, j])
                
    result = [-1, 10000001]
    for u in sorted(summits):
        if visited[u] < result[1]:
            result[0] = u
            result[1] = visited[u]
        
    return result