import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    my_flag = [list(map(str, input())) for _ in range(n)]

    min_num = n * m
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            cnt = 0
            for w in my_flag[:i+1]:
                for k in w:
                    if k != "W":
                        cnt += 1
            for b in my_flag[i+1:j+1]:
                for k in b:
                    if k != "B":
                        cnt += 1
            for r in my_flag[j+1:]:
                for k in r:
                    if k != "R":
                        cnt += 1
            if cnt < min_num:
                min_num = cnt

    print(min_num)
