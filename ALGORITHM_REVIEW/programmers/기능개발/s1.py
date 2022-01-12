def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        temp1 = 100 - progresses[i]
        temp2 = temp1 / speeds[i]
        if temp2 % 1:
            answer.append(temp1//speeds[i] + 1)
        else:
            answer.append(temp1//speeds[i])
    result = []
    cnt = 0
    temp = 0
    for j in range(len(answer)):
        if cnt == 0:
            temp = answer[j]
            cnt += 1
        else:
            if temp < answer[j]:
                result.append(cnt)
                cnt = 1
            else:
                cnt += 1
    result.append(cnt)
    # print(result)
    return result