def solution(prices):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/42584'''
    # 목표: O(n) 으로 풀기!!
    # 단조 스택 사용
    stack = [] # 처음 하락하는 시점을 아직 못 찾은 인덱스들
    answer = [0] * len(prices) # 하락 시점 찾고 기록
    
    for idx, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            n = stack.pop()
            answer[n] = idx - n
        
        stack.append(idx)
    
    # 하락 못 찾은 인덱스 처리
    while stack:
        n = stack.pop()
        answer[n] = len(prices) - n - 1
    
    return answer