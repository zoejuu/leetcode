def solution(queue1, queue2):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/118667'''
    # determine target
    total = sum(queue1) + sum(queue2)
    target = total // 2
    
    # impossible cases
    # 1. 총합이 홀수인 경우
    if total % 2 == 1:
        return -1
    # 2. 어느 한 원소가 타겟보다 클 경우
    if max(queue1 + queue2) > target:
        return -1
    
    cnt = 0
    s1 = sum(queue1)
    s2 = target - s1
    while s1 != s2:
        # operate FIFO
        if s1 > s2:
            x = queue1.pop(0)
            queue2.append(x)
            s1 -= x
            s2 += x
        elif s1 < s2:
            x = queue2.pop(0)
            queue1.append(x)
            s1 += x
            s2 -= x
        
        # impossible cases
        if not queue1 or not queue2:
            return -1
        
        cnt += 1
    return cnt

solution([3, 2, 7, 2], [4, 6, 5, 1])