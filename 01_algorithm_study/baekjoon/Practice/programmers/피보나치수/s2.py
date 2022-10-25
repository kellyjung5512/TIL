# DP로 풀어보라는 힌트 발견
# DP 기초를 알기 위해서 백준 1463, 9095 먼저 풀어봤다.
# DP 이해할 만 하다!

def solution(n):
    answer = 0
    dp = [0, 1, 1]
    if n > 2:
        for i in range(3, n+1):
            dp.append(dp[i-1] + dp[i-2])
    answer = dp[-1] % 1234567
    return answer