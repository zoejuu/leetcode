def solution(clothes):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/42578'''
    from collections import Counter

    clothes_ctr = Counter(cate for _, cate in clothes)    
    print(clothes_ctr)

    answer = 1

    for i in clothes_ctr.values():
        answer *= (i + 1)

    return answer - 1
    

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))