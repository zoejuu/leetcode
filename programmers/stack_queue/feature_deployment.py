def solution(progresses, speeds):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/42586'''
    import math
    
    features_per_day = [0]
    # days_required = (100 - progression) / speed
    days_required = []
    for i, (p, s) in enumerate(zip(progresses, speeds)):
        d = math.ceil((100 - p) / s)
        days_required.append(d)
    
    cur = days_required[0]
    for d in days_required:
        if d > cur:
            cur = d
            features_per_day.append(0)
        if d <= cur:
            features_per_day[-1] += 1
    
    return features_per_day