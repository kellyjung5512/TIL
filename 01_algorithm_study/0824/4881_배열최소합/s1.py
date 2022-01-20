import sys
sys.stdin = open('input.txt')

def find_min(col, temp):
    global min_num
    if temp > min_num:    # 도는 도중에 min_num보다 크면 계산 그만
        return

    if not 0 in visited:  # visited 꽉 차면 비교 후
        if temp < min_num:
            min_num = temp  # 현재 min_num보다 적으면 현재 값을 넣어줌

    for i in range(N):
        if not visited[i]:
            temp += numbers[col][i]
            visited[i] = 1
            find_min(col+1, temp)    # 재귀로 들어감
            visited[i] = 0           # 백트레킹
            temp -= numbers[col][i]

    return min_num

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_num = 9999999999
    ans = find_min(0, 0)
    # print(ans)
    print('#{} {}'.format(tc, ans))