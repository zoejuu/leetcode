def solution(maps):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/1844'''
    from collections import deque
    n = len(maps[0]) # 맵 가로길이
    m = len(maps) # 맵 세로길이
    start = (0,0) # 시작점
    target = (n-1, m-1) # 상대 진영
    
    dist = [[-1] * n for _ in range(m)] # 거리를 기록할 맵
    
    def bfs(start, target): # start = 시작 좌표 [x,y] | target = 목표 좌표
        queue = deque([start])
        move = [(1,0), (-1,0), (0,1), (0,-1)] # 동 서 남 북
        dist[0][0] = 1

        while queue:
            x, y = queue.popleft() # 기준 좌표

            if (x, y) == target: # 목표 도달 시 조기탈출
                return dist[y][x]

            for mx, my in move:
                nx, ny = x+mx, y+my
                if 0<=nx<n and 0<=ny<m: # 맵 밖
                    if maps[ny][nx] == 1 and dist[ny][nx] == -1: # 벽이거나 이미 방문한 곳이면 x
                        dist[ny][nx] = dist[y][x]+1 # 거리 계산
                        queue.append((nx, ny))
        return -1

    return bfs(start, target)
    

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))