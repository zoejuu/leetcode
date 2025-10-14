def solution(my_string):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/120902'''
    my_list = my_string.rsplit()
    answer = int(my_list[0])

    for i in range(len(my_list)):
        if i % 2 == 1:
            if my_list[i] == '+':
                answer += int(my_list[i+1])
            if my_list[i] == '-':
                answer -= int(my_list[i+1])
        
    return answer

print(solution("1234 + 1234"))