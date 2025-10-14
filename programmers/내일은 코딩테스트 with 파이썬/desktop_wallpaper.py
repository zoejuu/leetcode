def solution(wallpaper):
    files = []
    row = 0
    col = 0
    while row < len(wallpaper): # 파일 좌표 탐색
        if col >= len(wallpaper[0]):
            col = 0
            row += 1
            continue
        if wallpaper[row][col] == '#':
            files.append([row, col])
        col += 1
    
    files_x = [loc[0] for loc in files]
    files_y = [loc[1] for loc in files]
    
    lux = min(files_x) # 가장 왼쪽에 위치한 파일의 x값 = 가장 적은 x값
    luy = min(files_y) # 가장 위에 위치한 파일의 y값 = 가장 적은 y값
    rdx = max(files_x)+1 # 가장 오른쪽에 위치한 파일의 x값 = 가장 많은 x값+1
    rdy = max(files_y)+1 # 가장 아래에 위치한 파일의 y값 = 가장 많은 y값+1
    
    answer = [lux, luy, rdx, rdy]
    
    return answer

solution([".#...", "..#..", "...#."])