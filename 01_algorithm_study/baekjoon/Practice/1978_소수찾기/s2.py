# 2022-10-08

import sys
sys.stdin = open("input.txt")

N = int(input())
num_list = list(map(int, input().split()))
res = 0

for num in num_list:
    err = 0
    if num > 1:
        for tmp in range(2, num):
            if num % tmp == 0:
                err += 1
        if err == 0:
            res += 1

print(res)