def solution(participant, completion):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/42576'''
    from collections import Counter
    participant_count = Counter(participant)
    for person in completion:
        participant_count[person] -= 1
    return[person for person, cnt in participant_count.items() if cnt > 0][0]
    
solution(["leo", "kiki", "eden"],	["eden", "kiki"])