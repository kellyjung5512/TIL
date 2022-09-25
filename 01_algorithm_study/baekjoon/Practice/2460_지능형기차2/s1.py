import sys
sys.stdin = open("input.txt")

res = 0
cnt = 0
for _ in range(10):
    off_num, on_num = map(int, input().split())
    cnt = cnt + on_num - off_num
    if cnt > res:
        res = cnt

print(res)