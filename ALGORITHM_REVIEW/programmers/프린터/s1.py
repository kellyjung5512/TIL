def solution(priorities, location):
    answer = 0
    result = []
    for i in range(len(priorities)):
        result.append((priorities[i], i))
    result.sort(key=lambda x: x[0], reverse=True)
    print(result)
    return answer