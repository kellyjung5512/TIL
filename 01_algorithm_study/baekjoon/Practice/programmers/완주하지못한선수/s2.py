# 직관적으로 푸니까 쉽긴 한데 효율성에서는 거의 Zero...
# s1.py처럼 정렬 후에 문제를 푸는게 가장 좋을 듯

def solution(participant, completion):
    answer = ''
    for name in completion:
        for i in range(len(participant)):
            if name == participant[i]:
                participant.pop(i)
                break
    answer = participant[0]
    return answer