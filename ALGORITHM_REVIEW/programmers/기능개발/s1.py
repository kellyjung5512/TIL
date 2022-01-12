def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        temp1 = 100 - progresses[i]
        temp2 = temp1 / speeds[i]
        if temp2 % 1:
            answer.append(temp1//speeds[i] + 1)
        else:
            answer.append(temp1//speeds[i])
    print(answer)
    result = []
    cnt = 0
    temp = answer[0]
    for j in range(len(answer)):
        if temp < answer[j]:
            result.append(cnt)
            cnt = 1
        else:
            cnt += 1
    result.append(cnt)
    print(result)
    return result

a = [40, 93, 30, 55, 60, 65]
b = [60, 1, 30, 5, 10, 7]

print(solution(a, b))