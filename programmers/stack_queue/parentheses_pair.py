def solution(s):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/12909'''
    from collections import deque
    
    validation = deque(s)
    open = 0
    
    while validation:
        b = validation.popleft()
        if b == '(':
            open += 1
        elif b == ')':
            open -= 1
        if open < 0:
            return False
    if open != 0:
        return False
    return True