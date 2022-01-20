# 문제 풀이 시작 : 2021-10-27 20:20
# 문제 풀었는지? : YES / NO
# 문제를 풀었을 때 : 두 문제 중 왜 이 문제를 골랐는지?
# 문제를 풀지 못 했을 때 : 구하고자 하는 문제의 조건, input, output 제대로 이해하기, 어떻게 풀려고 노력했는지?
# 알아야 할 기본 개념? :

def make_road(arr, x):
    check_list = [0, 0]        # 오르막, 내리막 체크
    for i in range(1, len(arr)):
        # 오르막길일 때
        if arr[i] > arr[i-1]:
            if check_list[1] == 0:
                check_list[0] += 1
                if i != 1:
                    if arr[i-2] > arr[i-1]:
                        if check_list[1] >= x:
                            check_list[1] = 0
                            continue
                        else:
                            return 0
                    else:
                        continue


        # 내리막길일 때
        elif arr[i] < arr[i-1]:
            if check_list[0] == 0:
                check_list[1] += 1
                if i != 1:
                    if arr[i-2] < arr[i-1]:
                        if check_list[0] >= x:
                            check_list[0] = 0
                            continue
                        else:
                            return 0
                    else:
                        continue


        # 직진이면?
        elif arr[i] == arr[i-1]:
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
    print(mountain)
    for j in range(N):
        cnt += make_road(mountain[i], X)
    print(cnt)