def solution(queue1, queue2):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/118667'''
    cnt = 0
    while sum(queue1) != sum(queue2):
        # operate FIFO
        if sum(queue1) > sum(queue2):
            queue2.append(queue1.pop(0))
        elif sum(queue1) < sum(queue2):
            queue1.append(queue2.pop(0))
        
        # impossible cases
        if not queue1 or not queue2:
            return -1
        
        cnt += 1
    return cnt

solution([3, 2, 7, 2], [4, 6, 5, 1])