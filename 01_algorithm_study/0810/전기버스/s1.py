# 주유소 못들르는 것부터 체크하고 방문 횟수 체크해주기

import sys
sys.stdin = open('input.txt')

def run_station(location):
    cnt = 0
    for i in range(len(station)-1): # 주유소 거리 체크
        if station[i+1] - station[i] > K:
            return 0 # 안되면 바로 리턴

    else:
        while location < N: # 끝까지 갈 수 있을 때
            if location in station:
                cnt += 1
                location += K
            else:
                location -= 1
        return cnt # cnt 횟수 세기

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    location = K
    print('#{} {}'.format(tc, run_station(location)))