import sys
sys.stdin = open("input.txt")

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0, 1, 2, 4]
    if N > 3:
        for i in range(4, N+1):
            dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
    print(dp[N])