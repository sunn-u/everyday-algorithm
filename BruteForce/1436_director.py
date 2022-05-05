# https://www.acmicpc.net/problem/1436

n = int(input())

def end_number(n: int) -> int:
    # assertion.
    assert n >=1 and n <= 10000
    
    front_number, back_number = 0, 0
    back_length, back_limit, front_temp = 0, 0, 0
    state = 'front'
    for idx in range(n-1):
        if state == 'front':
            front_number += 1
            pos = str(front_number*100 + 66).find('666')
            if pos != -1:
                state = 'back'
                back_length = len(str(front_number)) - pos
                back_limit = 10**(back_length)
                front_temp = front_number // back_limit
                back_number = 0
        else:
            back_number += 1
            if back_number == back_limit:
                state = 'front'
                front_number += 1
    
    if state == 'front':
        return front_number*1000 + 666
    else:
        return (front_temp*1000 + 666)*back_limit + back_number
 
    # idx = 0
    # number = 666
    # while True:
    #     if '666' in str(number):
    #         idx += 1
    #         if n == idx:
    #             break
    #     number += 1
    # return number

number = end_number(n=n)
print(number)