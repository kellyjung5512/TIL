def solution(s):
    answer = list(map(str, s.split(" ")))
    result = ""
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            if j % 2 == 0:
                result += answer[i][j].upper()
            else:
                result += answer[i][j].lower()
        result += " "
    result = result[0:-1]
    return result