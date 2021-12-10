import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    password = list(map(int, input().split()))
    cnt = 1
    while password[-1] > 0:
        temp = password.pop(0)
        temp -= cnt
        cnt += 1
        if cnt >= 6:
            cnt = 1
        password.append(temp)
    password[-1] = 0
    print('#{} '.format(tc), end='')
    print(*password)