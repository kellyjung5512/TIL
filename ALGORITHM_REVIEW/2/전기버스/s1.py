import sys
sys.stdin = open('input.txt')

def run_station(location):
    cnt = 0
    for i in range(len(station)-1):
        if station[i+1] - station[i] > K:
            return 0

    else:
        while location < N:
            if location in station:
                cnt += 1
                location += K
            else:
                location -= 1
        return cnt

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    location = K
    print('#{} {}'.format(tc, run_station(location)))