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

    for cnt in fasion:
        answer = answer * (len(fasion[cnt]) + 1) # 안입는다 경우 더해서
    return answer - 1 # 아예 안입는 경우 하나 빼기

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))