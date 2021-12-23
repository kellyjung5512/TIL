import sys
sys.stdin = open('input.txt')

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = [0] * len(money)

    for i in range(len(money)):
        if N // money[i] >= 1:
            result[i] = N // money[i]
            N = N % money[i]

    print('#{}'.format(tc))
    print(*result)