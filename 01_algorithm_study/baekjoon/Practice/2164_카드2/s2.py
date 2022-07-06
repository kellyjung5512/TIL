# 시간 초과 해결하기...!
from collections import deque
import sys
sys.stdin = open('input.txt')

N = int(input())
card_list = deque([i for i in range(1, N+1)])

while len(card_list) > 1:
    card_list.popleft()
    tmp = card_list.popleft()
    card_list.append(tmp)

print(*card_list)