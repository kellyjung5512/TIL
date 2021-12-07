import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # for i in range(100, -1, -1):
    #     for j in range()