# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes_list: list) -> int:
    closet = dict()
    for clothes in clothes_list:
        _, kind = clothes
        if kind in closet:
            closet[kind] += 1
        else:
            closet[kind] = 2
    
    eval = 1
    for value in closet.values():
        eval *= value
    return eval - 1