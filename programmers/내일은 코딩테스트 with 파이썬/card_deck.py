from collections import deque
def solution(cards1, cards2, goal):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/159994'''
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    
    cur_card1 = cards1.popleft()
    cur_card2 = cards2.popleft()

    while len(goal) > 0:
        target = goal.popleft()

        if target == cur_card1:
            if len(cards1) == 0:
                cur_card1 = ""
            else:
                cur_card1 = cards1.popleft()
        elif target == cur_card2:
            print(len(cards2))
            if len(cards2) == 0:
                cur_card2 = ""
            else:
                cur_card2 = cards2.popleft()
        else:
            return "No"
    
    
    return "Yes"

print(solution(["i", "drink", "water"],	["want", "to"],	["i", "want", "to", "drink", "water"]))