def solution(bridge_length, weight, truck_weights):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/42583'''
    from collections import deque
    
    road = deque([[truck_weights[0], bridge_length]]) # length = bridge_length
    truck_weights = deque(truck_weights[1::])
    sec = 1
    
    while truck_weights or road:
        sec += 1
        for truck in road:
            truck[1] -= 1
        if road[0][1] == 0:
            road.popleft()
        if truck_weights:
            next = truck_weights[0]
            if sum(w[0] for w in road) + next <= weight and len(road) <= bridge_length:
                road.append([next, bridge_length])
                truck_weights.popleft()
    
    return sec