def solution(arr):    
    '''https://school.programmers.co.kr/learn/courses/30/lessons/12906'''
    answer = [arr[0]]
    for n in arr:
        if n != answer[-1]:
            answer.append(n)
    
    return answer