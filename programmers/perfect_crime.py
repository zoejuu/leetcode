def solution(info, n, m):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/389480'''
    dp = [121] * m
    dp[0] = 0

    for a_add, b_add in info:
        ndp = [121] * m
        
        for b in range(m):
            cur_a = dp[b]
            if cur_a == 121:
                continue
            # let A steal
            na = cur_a + a_add
            if na < n:
                if na < ndp[b]:
                    ndp[b] = na

            # let B steal
            nb = b + b_add
            if nb < m:
                if cur_a < ndp[nb]:
                    ndp[nb] = cur_a

        dp = ndp

            
    answer = min(dp)
    
    return -1 if answer == 121 else answer
    

print(solution([[1, 2], [2, 3], [2, 1]], 4, 4))