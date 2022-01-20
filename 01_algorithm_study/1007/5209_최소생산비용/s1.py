import sys
sys.stdin = open('input.txt')

# 런타임 에러가 뜬다 제기랄

from itertools import permutations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    number = [i for i in range(N)]
    number = list(permutations(number, N))
    result = 987654321

    while len(number) >= 0:
        temp = number.pop()
        x = 0
        y = 0
        ans = 0
        while len(temp) > y:
            ans += costs[x][temp[y]]
            x += 1
            y += 1
            if ans > result:
                break
        if ans < result:
            result = ans
        if len(number) == 0:
            break
    print('#{} {}'.format(tc, result))