import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    my_flag = [list(map(str, input())) for _ in range(n)]

    print(my_flag)