def months_notation(year_month_date):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/150370'''
    year, month, date = year_month_date.split(".")
    return (int(year)-2000)*12 + int(month) + (int(date)/100)

def is_expired(today, date_collected, duration):
    m_today = months_notation(today)
    m_date_collected = months_notation(date_collected)
    if m_today - m_date_collected >= duration:
        return True
    return False

def solution(today, terms, privacies):
    answer = []
    terms_dict = {term : int(duration) for term, duration in (t.split() for t in terms)} # term : duration
    privacies_list = [(d, t) for d, t in (p.split() for p in privacies)] # (date_collected, term)
    
    for i, privacy in enumerate(privacies_list):
        if is_expired(today, privacy[0], terms_dict[privacy[1]]):
            answer.append(i+1)
    
    return answer

solution("2022.05.19",	["A 6", "B 12", "C 3"],	["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])