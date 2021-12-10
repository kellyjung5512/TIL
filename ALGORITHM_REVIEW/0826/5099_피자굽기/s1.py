import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    oven = cheese[:N]
    left_cheese = cheese[N:]
    location = N
    idx_list = [i for i in range(len(oven))]

    while len(oven) > 1:
        temp = oven.pop(0) // 2
        idx = idx_list.pop(0)
        if temp > 0:
            oven.append(temp)
            idx_list.append(idx)
        else:
            if left_cheese:
                temp = left_cheese.pop(0)
                oven.append(temp)
                idx_list.append(N)
                N += 1
            else:
                continue
    print('#{} {}'.format(tc, idx_list[0]+1))