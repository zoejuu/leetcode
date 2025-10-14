def solution(answers):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/42840'''
    person_1 = [1,2,3,4,5]
    person_2 = [2,1,2,3,2,4,2,5]
    person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = {
        1 : 0,
        2 : 0,
        3 : 0
    }
    
    pointer = 0
    while pointer < len(answers):
        if answers[pointer] == person_1[pointer%5]:
            scores[1] += 1
        if answers[pointer] == person_2[pointer%8]:
            scores[2] += 1
        if answers[pointer] == person_3[pointer%10]:
            scores[3] += 1
        pointer += 1
    
    answer = [people for people, score in scores.items() if score == max(scores.values())]
        
    return answer

solution([1,2,3,4,4,5,6,6,7,8])