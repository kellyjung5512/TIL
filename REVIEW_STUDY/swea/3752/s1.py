# 문제 풀이 시작 : 2021-10-27 20:35 23:06
# 문제 풀었는지? : YES -> 하지만 런타임 에러 뜬다 ㅠㅠ
# 두 문제 중 왜 이 문제를 골랐는지? : 확실히 어떻게 풀어야할 지 감이 와서...? (조합만 알면 될 것 같아서)
# 문제를 풀지 못 했을 때 : 구하고자 하는 문제의 조건, input, output 제대로 이해하기, 어떻게 풀려고 노력했는지?
# 알아야 할 기본 개념? : 순열과 조합

import sys
sys.stdin = open('input.txt')

def print_set(n):
    global temp

    for i in range(n):                        # 각 부분 배열의 원소를 순회하며
        if check[i] == 1:                     # check[i]가 1이면 포함 되어있음을 의미하니
            temp += nums[i]          # 출력
    result.add(temp)
    temp = 0

def powerset(n, k):            # n: 현재 depth, k: 원소의 개수
    if n == k:
        print_set(n)
    else:
        check[n] = 1           # n번 요소를 포함시킴
        powerset(n+1, k)       # 다음 요소 포함 여부 결정하기 위한 호출
        check[n] = 0           # n번 요소를 포함시키지 않음
        powerset(n+1, k)       # 다음 요소 포함 여부 결정하기 위한 호출

T = int(input())
for tc in range(1, T+1):
    cnt_subset = 0
    N = int(input())
    nums = list(map(int, input().split()))
    check = [0 for _ in range(N)]
    temp = 0
    result = set()
    powerset(0, N)

    print('#{} {}'.format(tc, len(result)))