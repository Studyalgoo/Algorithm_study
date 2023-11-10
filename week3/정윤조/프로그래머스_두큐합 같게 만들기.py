"""
큐1 3 2 7 2  14 18 15
큐2 4 6 5 1  16 12 15

큐1 6  7  17 16 14 13 11 10
큐2 14 13  3 4  6  7  9  10

큐1 2 3 8 7 6 5 0  
큐2 6 5 0 1 2 3 8
"""
from collections import deque
def solution(queue1, queue2):
    answer=0
    queue1=deque(queue1)
    queue2=deque(queue2)
    hap1=sum(queue1)
    hap2=sum(queue2)
    lengths=len(queue1)+len(queue2)
    while answer<2*lengths:
        if hap1<hap2:
            num2=queue2.popleft()
            queue1.append(num2)
            hap1+=num2
            hap2-=num2
        elif hap1>hap2:
            num1=queue1.popleft()
            queue2.append(num1)
            hap1-=num1
            hap2+=num1
        else:
            break
        answer+=1    
    if answer==2*lengths:
        return -1
    return answer     