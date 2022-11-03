import sys
sys.stdin = open("input.txt")

N = int(input())
res = 0
for i in range(N):
    divide = list(map(int, str(i)))
    num = sum(divide) + i
    if num == N:
        res = i
        break
print(res)