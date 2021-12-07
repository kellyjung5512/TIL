import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    count_list = [0] * 5
    while N > 1:
        if N % 2 == 0:
            count_list[0] += 1
            N = N // 2
        elif N % 3 == 0:
            count_list[1] += 1
            N = N // 3
        elif N % 5 == 0:
            count_list[2] += 1
            N = N // 5
        elif N % 7 == 0:
            count_list[3] += 1
            N = N // 7
        elif N % 11 == 0:
            count_list[4] += 1
            N = N // 11
    print('#{} '.format(tc), end='')
    print(*count_list)