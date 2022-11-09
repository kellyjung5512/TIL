# 버블정렬: 서로 인접한 두 원소를 검사하여 정렬하는 알고리즘
# 장점: 구현이 매우 간단하다.
# 단점: 하나만 옮기려고 해도 다 교환되어야하는 번거로움, 순서에 맞지 않는 요소를 인접 요소로 교환
# 시간복잡도: O(n^2)

import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    tmp_list = list(map(int, input().split()))

    for i in range(N):
        for j in range(N-i-1):
            if tmp_list[j] > tmp_list[j+1]:
                tmp_list[j], tmp_list[j+1] = tmp_list[j+1], tmp_list[j]

    print(tmp_list)