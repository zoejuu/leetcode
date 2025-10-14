def solution(clothes):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/42578'''
    # clothes 를 딕셔너리로 만들기
    # dict = {카테고리 : [의상 리스트]}
    clothes_dict = {c[1] : list() for c in clothes}
    for i in range(len(clothes)):
        clothes_dict[clothes[i][1]].append(clothes[i][0])
    
    answer = 0
    categories = list(clothes_dict.keys())
    categories_cnt = len(categories)
    
    def dfs(n, outfit): # n = n번째 카테고리의 옷 | outfit = 겹치지 않는 옷 조합
        nonlocal answer
        if n == categories_cnt:
            answer += 1
            return
        items = clothes_dict[categories[n]] # 같은 종류의 옷들
        l = len(items)
        for i in range(l):
            outfit.add(items[i])
            answer += 1
            print(outfit)
            dfs(n+1, outfit)
            outfit.remove(items[i])
    
    dfs(0, set())
    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))