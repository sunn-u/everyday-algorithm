# https://www.acmicpc.net/problem/1541

n = input()
assert len(n) <= 50
assert n[0] not in ['+', '-'] and n[-1] not in ['+', '-']

def find_bracket(formula: str):
    formula_list = formula.split('-')
    results = []
    for chunk in formula_list:
        chunk_sum = sum(map(int, chunk.split('+')))
        results.append(chunk_sum)
    res = results[0] - sum(results[1:])

    # keep = ''
    # minus_time = False
    # for f in formula:
    #     if f not in ['+', '-']:
    #         keep += f
    #     else:
    #         if minus_time:
    #             keep = f'-{keep}'
    #         else:
    #             if f == '-':
    #                 minus_time = True
    #         res += int(keep)
    #         keep = ''
    # res = res - int(keep) if minus_time else  res + int(keep)
    
    return res

res = find_bracket(formula=n)
print(res)