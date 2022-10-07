import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    num_list = list(map(int, input().split()))

    # 정렬 해주기
    num_list.sort()
    print(num_list[7])
