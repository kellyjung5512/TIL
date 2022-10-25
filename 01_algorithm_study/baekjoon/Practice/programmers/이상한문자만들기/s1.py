# 분명 맞는 것 같은데 왜 테케 4개가 틀리는지 모르겠음

def solution(s):
    answer = list(map(str, s.split(" ")))
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            if j % 2 == 0:
                answer[i] = answer[i].replace(answer[i][j],answer[i][j].upper(), 1)
            else:
                answer[i] = answer[i].replace(answer[i][j],answer[i][j].lower(), 1)
    answer = " ".join(answer)
    return answer