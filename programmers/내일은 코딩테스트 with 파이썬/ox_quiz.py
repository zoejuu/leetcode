def solution(quiz):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/120907'''
    answer = []
    q_and_a = []
    for i in quiz:
        cur = i.rsplit(" = ")
        q_and_a.append(cur[0])
        q_and_a.append(cur[1])

    for i, expression in enumerate(q_and_a):
        if i % 2 == 0:
            my_list = expression.rsplit()
            cur_answer = int(my_list[0])

            for j in range(len(my_list)):
                if j % 2 == 1:
                    if my_list[j] == '+':
                        cur_answer += int(my_list[j+1])
                    if my_list[j] == '-':
                        cur_answer -= int(my_list[j+1])
        
            if cur_answer == int(q_and_a[i+1]):
                answer.append("O")
            else:
                answer.append("X")
            
    return answer

print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))