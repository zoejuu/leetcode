def solution(maps):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/1844'''
    n = len(maps[0]) # 맵 가로길이
    m = len(maps) # 맵 세로길이
    target = (n-1, m-1)
    d = []
    
    visited = [[False] * (n) for _ in range(m)]
    
    def dfs(i, x, y): # i = 이동횟수 x, y = 현재 좌표 [x, y]
        # 우측 하단에 다다르면 종료
        if (x, y) == target:
            d.append(i)
            return        
        
        visited[y][x] = True

        # 재귀
        move = ((1,0), (-1,0), (0,1), (0,-1)) # 동서남북
        for dx, dy in move:
            nx, ny = x+dx, y+dy
            # 벽이거나, 맵 밖이거나, 이미 방문한 곳이면 이동 불가
            if 0 <= nx < n and 0 <= ny < m:
                if maps[ny][nx] == 1 and not visited[ny][nx]:
                    dfs(i+1, nx, ny)

        # 백트래킹
        visited[y][x] = False
        
    dfs(1, 0, 0)
    print(d)

    if d:
        return min(d)
    else:
        return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))