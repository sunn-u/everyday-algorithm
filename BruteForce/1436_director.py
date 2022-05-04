# https://www.acmicpc.net/problem/1436

n = int(input())

def end_number(n: int) -> int:
    # assertion.
    assert n >=1 and n <= 10000
    
    idx = 0
    number = 666
    while True:
        if '666' in str(number):
            idx += 1
            if n == idx:
                break
        number += 1
    return number

number = end_number(n=n)
print(number)