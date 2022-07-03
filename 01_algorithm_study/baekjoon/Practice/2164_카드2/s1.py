# 앗 시간초과

import sys
sys.stdin = open('input.txt')

N = int(input())
card_list = [i for i in range(1, N+1)]

while len(card_list) > 1:
    card_list.pop(0)
    tmp = card_list.pop(0)
    card_list.append(tmp)

print(*card_list)