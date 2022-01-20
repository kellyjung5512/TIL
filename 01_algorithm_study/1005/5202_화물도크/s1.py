import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cars = [list(map(int, input().split())) for _ in range(N)]
    # print(cars)
    cars.sort(key=lambda x: x[1])
    cnt = 0
    temp = 0
    print(cars)
    for i in range(N):
        if temp <= cars[i][0]:
            cnt += 1
            temp = cars[i][1]
    print(cnt)