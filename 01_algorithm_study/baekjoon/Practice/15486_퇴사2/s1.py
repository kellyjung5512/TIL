import sys
sys.stdin = open('input.txt')

N = int(input())
arr = []
dp = [0] * (N+1)

for i in range(N):
  arr.append(list(map(int, input().split())))

res = 0

for j in range(N):
    res = max(res, dp[j])
    if j + arr[j][0] > N:
        continue
    dp[j+arr[j][0]] = max(res+arr[j][1], dp[j+arr[j][0]])

print(max(dp))