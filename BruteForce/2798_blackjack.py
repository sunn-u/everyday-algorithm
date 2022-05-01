# https://www.acmicpc.net/problem/2798

n, m = map(int, input().split())
card_numbers_list = list(map(int, input().split()))

def blackjack(n:int, m:int, card_list: list):
    # assertion.
    assert n == len(card_list)
    assert n >= 3 and n <= 100 and m >= 10 and m <= 300000
    for card_num in card_list:
        assert card_num > 0 and card_num < 100000
    
    results = []
    for a in range(n-2):
        for b in range(a+1, n-1):
            for c in range(b+1, n):
                tmp = card_list[a] + card_list[b] + card_list[c]
                if tmp <= m:
                    results.append(tmp)
                    
    #     results = []
    # for a in card_list:
    #     for b in card_list:
    #         if b == a:
    #             continue
    #         for c in card_list:
    #             if c == a or c == b:
    #                 continue
    #             tmp = a + b + c
    #             if tmp <= m:
    #                 results.append(tmp)
                    
    return max(results)

    
result = blackjack(n=n, m=m, card_list=card_numbers_list)
print(result)
