# https://www.acmicpc.net/problem/11399

n = int(input())
assert n >= 1 and n <= 1000
time_list = list(map(int, input().split()))
assert n == len(time_list)
for time in time_list:
    assert time >= 1 and time <= 1000

def atm(n: int, time_list: list) -> int:
    # selection sort.
    for idx in range(n):
        min = time_list[idx]
        min_idx = idx
        for inner_idx in range(idx, n):
            if time_list[inner_idx] < min:
                min = time_list[inner_idx]
                min_idx = inner_idx
        time_list[idx], time_list[min_idx] = time_list[min_idx], time_list[idx]
    
    result = sum([time*(n-idx) for idx, time in enumerate(time_list)])
    return result

result = atm(n=n, time_list=time_list)
print(result)
