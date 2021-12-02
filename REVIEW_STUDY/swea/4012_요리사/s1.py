# 문제 풀이 시작 : 2021-11-09 23:16
# 문제 풀었는지? : YES / NO
# 문제를 풀었을 때 : 두 문제 중 왜 이 문제를 골랐는지?
# 문제를 풀지 못 했을 때 : 구하고자 하는 문제의 조건, input, output 제대로 이해하기, 어떻게 풀려고 노력했는지?
# 알아야 할 기본 개념? : 부분집합 만들기?

import sys
from itertools import combinations

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())     # 식재료 수
    food_list = [list(map(int, input().split())) for _ in range(N)]
    # print(food_list)
    man = [1, 2, 3, 4]
    result = []
    a = combinations(man, N)
    result.extend(a)
    print(result)
