def solution(priorities, location):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/42587'''
    from collections import deque
    
    queue = deque([(i, priorities) for i, priorities in enumerate(priorities)])
    
    cnt = 0
    while queue:
        cur_process = queue.popleft()
        if any(cur_process[1] < process[1] for process in queue):
            queue.append(cur_process)
        else:
            cnt += 1
            if cur_process[0] == location:
                break
    
    return cnt