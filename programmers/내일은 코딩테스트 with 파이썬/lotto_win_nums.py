def solution(lottos, win_nums):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/77484'''
    matching_count = 0
    unknown_count = 0
    confirmed_nums = []
    
    for num in lottos:
        if num == 0:
            unknown_count += 1
        else:
            confirmed_nums.append(num)
    
    for num in confirmed_nums:
        if num in win_nums:
            matching_count += 1
    
    answer = []
    # 최고
    if (6 - (matching_count + unknown_count) + 1) > 6:
        answer.append(6)
    else:
        answer.append(6 - (matching_count + unknown_count) + 1)
    # 최저
    if (6 - matching_count + 1) > 6:
        answer.append(6)
    else:
        answer.append(6 - matching_count + 1)
    
    return answer