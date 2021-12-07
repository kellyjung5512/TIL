import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    check = []

    # 행 전체 합
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += arr[i][j]
        check.append(temp)

    # 열 전체 합
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += arr[j][i]
        check.append(temp)

    # 왼->오 합
    for i in range(100):
        temp = 0
        temp += arr[i][i]

    # 오->왼 합
    for i in range(100):
        temp = 0
        temp += arr[i][99-i]

    print('#{} {}'.format(tc, max(check)))