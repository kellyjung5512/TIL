import sys
sys.stdin = open('input.txt')

def find_min(idx, cnt):
    global result

    if cnt >= result:
        return

    if idx+1 >= len(station):
        if result > cnt:
            result = cnt
        return

    for i in range(idx+station[idx], idx-1, -1):
        find_min(i, cnt + 1)

T = int(input())
for tc in range(1, T+1):
    station = list(map(int, input().split()))
    N = station.pop(0)
    result = 987654321
    find_min(0, -1)

    print(result)
