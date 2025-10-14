def solution(picks, minerals):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/172927'''
    hp = 0 # 피로도
    picks = {'diamond' : picks[0], 'iron' : picks[1], 'stone' : picks[2]}
    hp_per_mineral = {'diamond' : 25, 'iron' : 5, 'stone' : 1}
    hp_per_pick = {'diamond' : 0.04, 'iron' : 0.2, 'stone' : 1}
    
    # 광물 리스트를 다섯개씩 쪼개기 (한번에 캘수있는 광물들)
    minerals_per_mine = []
    idx = 0
    for i in range(0, len(minerals), 5):
        minerals_per_mine.append([])
        for j in range(i, i+5):
            if j >= len(minerals):
                break
            minerals_per_mine[idx].append(hp_per_mineral[minerals[j]])
        idx += 1
        
    minerals_per_mine.sort(key = lambda n : -sum(n))

    diff = len(minerals_per_mine) - sum(picks.values())
    if diff > 0:
        for i in range(diff):
            del minerals_per_mine[i]
    
    hp_total = 0
    for minerals_to_mine in minerals_per_mine:
        # 사용 가능한 곡괭이가 없으면 종료
        if len([durability for durability in picks.values() if durability > 0]) == 0:
            break
        # 곡괭이 배정 (높은 피로도를 요구하는 광물 세트부터 높은 티어의 곡괭이 배정)
        cur_pick = 0
        for m in ('diamond', 'iron', 'stone'):
            if picks[m] > 0:
                picks[m] -= 1
                cur_pick = hp_per_pick[m]
                break
                
        # 배정된 곡갱이를 이용하여 광물 캐고 피로도 누적
        for mineral in minerals_to_mine:
            hp_required = mineral * cur_pick
            if hp_required < 1: hp_total += 1
            else: hp_total += hp_required
    
    return int(hp_total)

print(solution([0, 1, 1],	["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))