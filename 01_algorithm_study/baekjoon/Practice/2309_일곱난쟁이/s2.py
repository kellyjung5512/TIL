import sys
from itertools import combinations
sys.stdin = open("input.txt")

num_list = [int(input()) for _ in range(9)]
res = []
for i in combinations(num_list, 7):
    if sum(i) == 100:
        res = sorted(i)
        print(res)
        break
        # for j in sorted(i):
        #     print(j)
        # break