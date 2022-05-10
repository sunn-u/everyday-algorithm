# https://programmers.co.kr/learn/courses/30/lessons/87389

def solution(n: int) -> int:
    # assertion.
    assert n >= 3 and n <= 1000000
    
    tmp = n - 1
    for idx in range(2, (tmp//2)+1):
        if tmp % idx == 0:
            return idx
    return tmp
        
    # tmp = n - 1
    # if tmp % 2 == 0:
    #     return 2
    # else:
    #     for idx in range(3, n+1):
    #         if tmp % idx == 0:
    #             return idx
    #     return tmp