# 틀렸음 다시 해봐야 함
import sys
sys.stdin = open('input.txt')

N = int(input())
for _ in range(N):
    M = int(input())
    box_list = list(map(int, input().split()))
    max_box = 0
    cnt = 1
    res = 0
    for box in box_list:
        if box >= max_box:
            max_box = box
            if res < cnt:
                res = cnt
            cnt = 1
        else:
            cnt += 1

    print(res)