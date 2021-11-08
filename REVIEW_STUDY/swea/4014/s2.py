def make_road(arr, x):
    check = 0
    cnt = 1
    idx = 1
    while idx < len(arr):
        if arr[idx] < arr[idx-1]: # 내리막길이면
            num = arr[idx]
            while arr[idx+cnt] == num:
                cnt += 1
                check += 1
            if check >= x:
                cnt = 0
                check = 0
                idx += 1
                continue
            else:
                return 0

        elif arr[idx] > arr[idx-1]: # 오르막길이면
            num = arr[idx]
            while arr[idx+cnt] == num:
                cnt += 1
                check += 1
            if check >= x:
                cnt = 0
                check = 0
                idx += 1
                continue
            else:
                return 0

        else:
            idx += 1
            continue

        return 1

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())          # N: 지도 한 변의 크기, X: 경사로의 길이
    mountain = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        cnt += make_road(mountain[i], X)
    mountain = list(map(list, zip(*mountain)))
    # print(mountain)
    for j in range(N):
        cnt += make_road(mountain[i], X)
    print(cnt)