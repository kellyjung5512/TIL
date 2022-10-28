import sys
sys.stdin = open("input.txt")
from itertools import combinations

while True:
    S = list(map(int, input().split()))
    if S[0] == 0:
        break
    S_list = S[1:]
    result = list(combinations(S_list, 6))

    for i in range(len(result)):
        print(*result[i])
    print()
