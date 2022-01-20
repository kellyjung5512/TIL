def solution(participant, completion):
    completion.sort()
    participant.sort()
    answer = participant[-1]
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            answer = participant[i]
            break
    return answer