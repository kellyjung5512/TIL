import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    node = [list(input().split()) for _ in range(N)]

    print(node)