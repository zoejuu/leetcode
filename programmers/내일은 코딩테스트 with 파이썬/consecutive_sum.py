def solution(num, total):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/120923'''
    answer = []
    a = 0
    for i in range(num):
        a += i
    start = (total - a) // num
    for j in range(num):
        answer.append(start+j)
    return answer

print(solution(3, 12))