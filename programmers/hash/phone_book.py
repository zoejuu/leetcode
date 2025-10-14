def solution(phone_book):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/42577'''
    numbers_set = set(phone_book)
    for number in phone_book:
        i = 1
        while i < len(number):
            if number[:i] in numbers_set:
                return False
            i += 1
    
    return True