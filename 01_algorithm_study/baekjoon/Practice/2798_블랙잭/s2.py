import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
card_list = list(map(int, input().split()))
res = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            num = card_list[i] + card_list[j] + card_list[k]
            if num > M:
                continue
            else:
                if res > num:
                    continue
                else:
                    res = num
print(res)