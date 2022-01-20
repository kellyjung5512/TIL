import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N, number = map(str, input().split())
    number = list(number)
    # print(number)
    stack = []
    for i in range(len(number)):
        if stack and number[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(number[i])
    print('#{} '.format(tc),end='')
    print(''.join(stack))