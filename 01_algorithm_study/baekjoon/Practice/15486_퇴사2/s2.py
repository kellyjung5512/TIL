import sys

N = int(sys.stdin.readline())       # 왜 sys & stdin & readline() 쓰는걸까?

day = N
T, P = [], []
dp = [0] * (N + 1)

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    T.append(temp[0])
    P.append(temp[1])

for i in range(0, N):
    if T[i] <= N - i:       # 일할 날이 남아있는 경우
        dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])      # 다음에 일할 수 있는 날에 받은 pay를 입력

    dp[i + 1] = max(dp[i + 1], dp[i])                       # 각각 시작한 위치를 다르게 잡아서 pay가 가장 큰 것을 기록
print(dp[N])  