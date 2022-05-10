# https://www.acmicpc.net/problem/7568

n = int(input())
xy_list = []
for idx in range(n):
    x, y = tuple(map(int, input().split()))
    assert x >= 10 and y <= 200
    xy_list.append((x, y))

def compare_body(n: int, xy_list: list) -> list:
    #assertion.
    assert n >= 2 and n <= 50
    
    results = [1] * n
    length = len(xy_list)
    for a in range(length):
        a_x, a_y = xy_list[a]
        for b in range(a+1, length):
            b_x, b_y = xy_list[b]
            
            if a_x > b_x and a_y > b_y:
                results[b] += 1
            elif a_x < b_x and a_y < b_y:
                results[a] += 1
            else:
                pass
    return results

results = compare_body(n=n, xy_list=xy_list)
print(*results)
# result = ""
# for idx in results:
#     result += f"{str(idx)} "
# print(result.strip())