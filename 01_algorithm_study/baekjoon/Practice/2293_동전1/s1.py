import sys
import itertools
sys.stdin = open('input.txt')


n, k = map(int, input().split())
coin = list()
for _ in range(n):
    coin.append(int(input()))

