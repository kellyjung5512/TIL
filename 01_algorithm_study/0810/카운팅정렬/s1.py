# 카운팅 정렬:
import sys
sys.stdin = open("input.txt")

T = int(input())
 for tc in range(T):
    N = int(input())
    result = [0] * N
    tmp_list = list(map(int, input().split()))
    counter = [0] * 10

    for tmp in tmp_list:
        counter[tmp] += 1

    for i in range(1, len(counter)):
        counter[i] += counter[i-1]

     for num in tmp_list:
        idx = counter[num]
        result[idx - 1] = num
        counter[num] -= 1

    print(result)