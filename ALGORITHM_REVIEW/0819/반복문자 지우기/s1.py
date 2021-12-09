import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    s = list(map(str, input()))
    stack = []
    for i in range(len(s)):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
    print('#{} {}'.format(tc, len(stack)))