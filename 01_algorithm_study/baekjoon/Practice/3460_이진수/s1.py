import sys
sys.stdin = open("input.txt")

T = int(input())
for _ in range(T):
    n = int(input())
    tmp = 0
    res = []
    while n >= 1:
        if n % 2 == 1:
            res.append(tmp)
        n = n // 2
        tmp += 1
    print(*res)