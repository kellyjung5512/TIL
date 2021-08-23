import sys
sys.stdin = open('input.txt')

cnt_list = [[0] * 100 for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            cnt_list[i][j] += 1
cnt = 0
for i in range(len(cnt_list)):
    for j in range(len(cnt_list[i])):
        if cnt_list[i][j] > 0:
            cnt += 1

print(cnt)
