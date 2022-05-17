# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name: str) -> int:
    # assertion.
    assert len(name) >=1 and len(name) <= 20
    for n in name:
        assert n.isupper()
        
    # fixed-vairables.
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_dict = {a: 26 - idx if idx > 13 else idx for idx, a in enumerate(alphabet)}
    
    answer = 0
    for n in name:
        step = alphabet_dict[n]
        answer += step
    answer += len(name) - 1
    
    if name[1] == "A":
        for n in name[1:]:
            if n != "A":
                break
            answer -= 1
        return answer
    else:
        if name[-1] == "A":
            for n in name[1:][::-1]:
                if n != "A":
                    break
                answer -= 1
            return answer
    return answer

# "BBBBAAAABA" = 12
name = "BBBBAAAABA" #"JEAAAAAAAAAAA" #"JAAAAAAAAAZ" 
answer = solution(name=name)
print(answer)