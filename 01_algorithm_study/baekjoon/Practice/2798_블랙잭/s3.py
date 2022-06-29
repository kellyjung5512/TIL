#combination으로 푸는 법 도전! ==> 성공~!

import sys
sys.stdin = open('input.txt')
from itertools import combinations

N, M = map(int, input().split())
card_list = list(map(int, input().split()))
combi_card_list = list(combinations(card_list, 3))
res = 0
for combi in combi_card_list:
    num = sum(combi)
    if num > M:
        continue
    else:
        if num > res:
            res = num
        else:
            continue
print(res)