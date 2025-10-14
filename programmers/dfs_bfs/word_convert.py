def solution(begin, target, words):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/43163'''
    from collections import deque
    # edge case
    if target not in words:
        return 0
    
    l = len(begin)
    begin_chars = [c for c in begin[::1]]
    target_chars = [c for c in target[::1]]
    queue = deque([(begin_chars, 0)])
    
    while queue:
        cur_chars, step = queue.popleft()
        
        # cur_chars 가 target_chars 와 동일하면 조기 종료
        if cur_chars == target_chars:
            return step
        
        # 한글자만 다른 단어가 리스트에 있다면 그 단어를 큐에 추가
        # [['h', 'i', 't'] ['h', 'o', 't']]
        for word in words:
            word_chars = [c for c in word[::1]]
            diff = 0
            for i in range(l):
                if cur_chars[i] != word_chars[i]:
                    diff += 1
                if diff >= 2:
                    break
            if diff < 2:
                queue.append((word_chars, step+1))
    
    return 0