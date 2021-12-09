import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus_info = [list(map(int, input().split())) for _ in range(N)]
    bus_station = [0] * 5001
    # print(bus_info)
    for i in range(len(bus_info)):
        start = bus_info[i][0]
        end = bus_info[i][1]
        for j in range(start, end+1):
            bus_station[j] += 1
    # print(bus_station)
    P = int(input())
    find_bus = [int(input()) for _ in range(P)]
    ans = []
    for k in range(len(find_bus)):
        ans.append(bus_station[find_bus[k]])
    print('#{} '.format(tc), end='')
    print(*ans)