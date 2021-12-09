import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    Forth = list(map(str, input().split()))
    stack = []
    ans = 0
    for i in range(len(Forth)-1):
        if Forth[i].isdigit():
            stack.append(Forth[i])
        else:
            try:
                b, a = int(stack.pop()), int(stack.pop())
                if Forth[i] == '+':
                    temp = a + b
                elif Forth[i] == '-':
                    temp = a - b
                elif Forth[i] == '*':
                    temp = a * b
                elif Forth[i] == '/':
                    temp = a // b
                stack.append(temp)
            except:
                ans = 'error'
    if len(stack) == 1:
        ans = stack.pop()
    else:
        ans = 'error'

    print('#{} {}'.format(tc, ans))