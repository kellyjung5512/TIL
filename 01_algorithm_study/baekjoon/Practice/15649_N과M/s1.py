# 다시 풀기 ^___^
from itertools import combinations
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
num_list = [str(i) for i in range(1, N+1)]
# combi_list = list(combinations(num_list, M))
# print(combi_list)
for i in range(N):
    map(int, input().split())
    print("".join(list(map("".join, combinations(num_list, M))))[i])
    # join(함수가 들어가는 위치, 리스트 같은 input 값)
