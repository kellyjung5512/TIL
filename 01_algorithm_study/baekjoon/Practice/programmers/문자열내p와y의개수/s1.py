# 처음에 푼 코드

def solution(s):
    answer = False
    p_num = 0
    y_num = 0
    for i in s:
        if i == "p" or i == "P":
            p_num += 1
        elif i == "y" or i == "Y":
            y_num += 1
    if p_num == y_num:
        answer = True
    return answer