# 어쩜 이렇게도 같은지~
# 다른 사람들 풀이 보면서 새로운 내용 공부해보기

def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == ")":
            if len(stack) > 0:
                stack.pop()
            else:
                answer = False
        else:
            stack.append("(")
    if len(stack) > 0:
        answer = False
    return answer