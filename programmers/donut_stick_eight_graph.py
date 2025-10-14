def solution(edges):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/258711'''
    from collections import Counter
    # 1) 허브 찾기 (생성된 정점)
    # 조건: indegree 없이 outdegree만 있는 정점, outdegree 최소 두개 이상
    starts, ends = zip(*edges)
    starts_cnt = Counter(starts)
    ends_set = set(ends)
    vertices = set(starts+ends) # 정점들
    hub = next(v for v in vertices if v not in ends_set and starts_cnt[v] >= 2) # 허브
    
    # 2) 허브 간선 제외 후, 각 정점의 outdegree indegree 집계
    # dict = {vertex : [outdegree, indegree]}
    graph_edges = {tuple(e) for e in edges if e[0] != hub} # 허브 간선을 제외한 나머지 간선 (그래프 간선)
    graph_edges_map = {v : [0,0] for v in vertices if v != hub}
    for u, v in graph_edges:
        graph_edges_map[u][0] += 1 #outdegree
        graph_edges_map[v][1] += 1 #indegree
    
    # 3) 각 그래프 갯수 집계
    sticks, eights = 0, 0
    for e in graph_edges_map.values():
        if e == [1,0] or e == [0,0]:
            # 막대 그래프의 특징은 시작 정점(1,0), 끝 정점 (0,1) 제외하고 모두 (1,1) | 또는 정점 하나일 시 (0,0)
            sticks += 1
        elif e == [2,2]:
            # 8자 그래프의 특징은 중심 정점(2,2) 제외 모두 (1,1)
            eights += 1
    # 도넛 그래프의 특징은 모든 정점이 (1,1) -> 총 그래프 수 - (막대 그래프 수 + 8자 그래프 수)
    donuts = starts_cnt[hub] - (sticks + eights)
    
    return [hub, donuts, sticks, eights]

print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))