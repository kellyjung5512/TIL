import sys
sys.stdin = open("input.txt")

N, M, K = map(int, input().split())
roadmap = [[] for _ in range(N + 1)]

for _ in range(K):
    pass