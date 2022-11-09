import sys
sys.stdin = open('input.txt')

N = int(input())
for _ in range(N):
    M = int(input())
    box_list = list(map(int, input().split()))
    max_box = 0
    res = 0
    for i in range(len(box_list) - 1):
        cnt = 0
        parts = box_list[i:]
        for part in parts:
            if part < box_list[i]:
                cnt += 1
        if res < cnt:
            res = cnt

    print(res)