from collections import Counter
def solution(nums):
    '''https://school.programmers.co.kr/learn/courses/30/lessons/1845'''
    capability = len(nums) // 2
    pokemons = set(nums)
    if len(pokemons) >= capability:
        return capability
    else:
        return len(pokemons)