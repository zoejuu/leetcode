def solution(N, number):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/42895'''
    # dp 리스트의 원소는 N을 1..8번 사용해서 만들 수 있는 정수들의 집합
    # dp = [set(), set(), set()...]
    dp = [set() for _ in range(9)] 
    
    for k in range(1, 9):
        # k -> 1 2 3 4 5 6 7 8
        dp[k].add(int(str(N) * k))
        
        for i in range(1, k):
            # k = 4 | i = 1, 2, 3 | j = 3, 2, 1
            j = k - i
            for x in dp[i]: # 이전 값들을 불러옴
                for y in dp[j]:
                    dp[k].add(x + y)
                    dp[k].add(x - y)
                    dp[k].add(x * y)
                    dp[k].add(x // y)
                    dp[k] -= {num for num in dp[k] if num <= 0 or num >= 32000}
        if number in dp[k]:
            return k
    
    return -1