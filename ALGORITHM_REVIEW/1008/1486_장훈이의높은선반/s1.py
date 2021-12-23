import sys
sys.stdin = open('input.txt')

from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    temp_list = []
    for i in range(1, N+1):
        c = combinations(height, i)
        temp_list.extend(c)
    # print(temp_list)

    result = []
    for j in range(len(temp_list)):
        temp = 0
        for k in range(len(temp_list[j])):
            temp += temp_list[j][k]
        if temp >= B:
            result.append(temp)
    # print(result)
    print('#{} {}'.format(tc, min(result)-B))