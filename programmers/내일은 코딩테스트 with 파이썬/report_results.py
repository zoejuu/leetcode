from collections import defaultdict
def solution(id_list, report, k):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/92334'''
    # determine who's account is suspended
    reported = defaultdict(set) # reportee : [reporters]
    for r in report:
        r = r.split(" ")
        reporter, reportee = r[0], r[1]
        reported[reportee].add(reporter)
    suspended = {reportee : reporters for reportee, reporters in reported.items() if len(reporters) >= k }
    
    # determine mailing
    mail_list = []
    for i in range(len(id_list)):
        mail_list.append(0)
        for reporters in suspended.values():
            if id_list[i] in reporters:
                mail_list[i] += 1
    
    return mail_list
print(solution(["con", "ryan"],	["ryan con", "ryan con", "ryan con", "ryan con"],	3))