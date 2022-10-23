def solution(progresses, speeds):
    result = []
    time = 0
    cnt = 0
    while len(progresses) > 0:
        if progresses[0] + time * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                result.append(cnt)
                cnt = 0
            time += 1
    result.append(cnt)
    return result

solution([93, 30, 55], [1, 30, 5])