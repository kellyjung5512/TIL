def solution(clothes):
    fasion = {}
    answer = 1
    for temp in clothes:
        key = temp[1]
        value = temp[0]
        if key in fasion:
            fasion[key].append(value)
        else:
            fasion[key] = [value]

    for cnt in fasion.keys():
        answer = answer * (len(fasion[cnt]) + 1)
    return answer - 1