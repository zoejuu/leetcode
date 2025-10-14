def solution(genres, plays):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/42579'''
    answer = []
    # determine which genre comes first
    genres_streaming = dict()
    for i in range(len(genres)):
        genres_streaming[genres[i]] = genres_streaming.get(genres[i], 0) + plays[i]
    
    genres_sorted = list()
    while len(genres_streaming) > 0:
        genres_sorted.append(
            next(g for g, p in genres_streaming.items() if p == max(genres_streaming.values()))
        )
        genres_streaming.pop(genres_sorted[-1])
    
    # create dict for each genre
    done = set()
    for genre in genres_sorted:
        if genre in done: continue
        song_list = {i : p for i, (g, p) in enumerate(zip(genres, plays)) if g == genre}
        done.add(genre)

        # pick top two songs
        top_two = []
        while len(top_two) < 2 and len(song_list) > 0:
            top_two.append(
                next(i for i, p in song_list.items() if p == max(song_list.values()))
            )
            song_list.pop(top_two[-1])
        answer.extend(top_two)
    
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],	[500, 600, 150, 800, 2500]))