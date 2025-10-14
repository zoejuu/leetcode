from itertools import product
def solution(numbers, target):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/389480'''
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

print(solution([1,2,3,4,5], 5))