import sys
sys.stdin = open("input.txt")

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0 for i in range(k+1)]
dp[0] = 1


print(coins)