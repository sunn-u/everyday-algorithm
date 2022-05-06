# https://www.acmicpc.net/problem/2750

n = int(input())
assert n >=1 and n <= 1000
n_list = []
for idx in range(n):
    num = int(input())
    assert num <= 1000 and num >= -1000
    n_list.append(num)
    
def sorting(n:int, n_list: list) -> list:
    for idx in range(1, n):
        num = n_list[idx]
        insert = idx
        for inner_idx in range(1, idx+1):
            if n_list[idx] < n_list[idx - inner_idx]:
                insert = idx - inner_idx
            else:
                break
        del n_list[idx]
        n_list.insert(insert, num)
    return n_list

    # results = [n_list[0]]
    # for idx, num in enumerate(n_list[1:]):
    #     idx += 1
    #     insert = False
    #     for search in range(idx):
    #         if num < results[search]:
    #             results.insert(search, num)
    #             insert = True
    #             break
    #     if not insert:
    #         results.insert(search + 1, num)
    # return results

results = sorting(n=n, n_list=n_list)
# print.
for res in results:
    print(res)
