# 한번에 통과 완료 ^__^

def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i.isnumeric() == False:
                answer = False
                break
    else:
        answer = False
    return answer