def solution(clothes):
    answer = 1
    tmp = {}
    for i in range(len(clothes)):
        tmp[clothes[i][1]] = tmp.get(clothes[i][1], []) + [clothes[i][0]]

    for j in tmp:
        answer *= (len(tmp[j]) + 1)

    return answer - 1