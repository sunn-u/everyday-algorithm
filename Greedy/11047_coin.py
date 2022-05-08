# https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())
assert n >= 1 and n <= 10
coin_list = []
for idx in range(1, n+1):
    coin = int(input())
    # assertion.
    assert coin >= 1 and coin <= 1000000
    if idx == 1:
        assert coin == 1
    else:
        assert coin > coin_list[idx-2] and coin % coin_list[idx-2] == 0
    coin_list.append(coin)
    
def minimal_coin(coin_list: list, k: int) -> int:
    result = 0
    
    # for coin in coin_list[::-1]:
    #     result += k // coin
    #     k %= coin
    #     if k == 0:
    #         break
        
    for coin in coin_list[::-1]:
        need = k // coin
        if need >= 1:
            k -= need * coin
            result += need
        
        # only for break.
        last = k % coin
        if last == 0:
            break
        
    return result

res = minimal_coin(coin_list=coin_list, k=k)
print(res)