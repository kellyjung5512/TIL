N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N+1)

largest = 0
for i in range(N):
    t, p = table[i]
    largest = max(largest, dp[i])

    if t + i > N:   # N+1 일째부터는 회사가 없어 상담 불가
        continue

    dp[i+t] = max(largest + p, dp[i+t])

print(max(dp))