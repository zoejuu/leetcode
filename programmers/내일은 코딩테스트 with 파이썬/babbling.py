def solution(babbling):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/120956'''
    answer = 0
    babbles = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        for babble in babbles:
            b = b.replace(babble, "0")
            if len(b.replace("0", "")) == 0:
                answer += 1
                break
    
    return answer

print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))