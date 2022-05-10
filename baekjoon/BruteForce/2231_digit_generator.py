# https://www.acmicpc.net/problem/2231

n = int(input())

def digit_generator(n: int) -> int:
    # assertion.
    assert n >= 1 and n <= 1000000

    min_n = n - (len(str(n))*9)
    if min_n < 0:
        min_n = 0
    
    for num in range(min_n, n):
        tmp = num + sum([int(i) for i in str(num)])
        if tmp == n:
            return num
    return 0

    # results = []
    # for num in range(n, 0, -1):
    #     tmp = num + sum([int(i) for i in str(num)])
        
    #     if tmp == n:
    #         results.append(num)
    # return min(results) if len(results) != 0 else 0

result = digit_generator(n=n)
print(result)
