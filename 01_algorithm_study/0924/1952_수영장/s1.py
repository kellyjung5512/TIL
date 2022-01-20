import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    result = []