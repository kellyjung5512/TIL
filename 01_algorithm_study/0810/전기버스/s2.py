# 조금만 더 고치면 될 것 같은데...!!

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split())
    bus_stop = [0] * N
    charger = list(map(int, input().split()))
    bus = 0
    cnt = 0
    res = 0
    while bus < N:
        cnt += 1
        bus += K
        if bus >= N:
            res = cnt
        elif bus in charger:
            continue
        else:
            for i in range(K-1):
                bus -= 1
                if bus in charger:
                    break

    print(res)

