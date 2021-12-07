import sys
sys.stdin = open('input.txt')

def is_correct(temp):
    for i in range(len(temp)):
        if temp[i] == "(":
            stack.append("(")
        elif temp[i] == "{":
            stack.append("{")
        elif temp[i] == ")" and stack[-1] == "(":
            stack.pop()
        elif temp[i] == "}" and stack[-1] == "{":
            stack.pop()
    if stack:
        return 0
    else:
        return 1

T = int(input())
for tc in range(1, T+1):
    str_list = list(map(str, input()))
    stack = []
    print('#{} {}'.format(tc, is_correct(str_list)))