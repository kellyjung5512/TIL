# 태훈
import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):

    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    record = ['W'] + [0] * (N-2) + ['R']
    # 첫줄과 마지막줄은 미리 페인트
    ans = flag[0].count('B') + flag[0].count('R') + flag[-1].count('W') + flag[-1].count('B')

    for i in range(1, N-1):
        w, b, r = flag[i].count('W'), flag[i].count('B'), flag[i].count('R')
        if i+1 == N-1:                                              # 마지막에서 두번째 칸일 경우
            if record[i-1] != 'R':                                  # 파란색 & 빨간색 페인트 가능 할때
                if b >= r:                                          # 파란색 페인트 많이 되어있으면
                    ans += flag[i].count('W') + flag[i].count('R')  # 파랗게 페인트
                    record[i] = 'B'
                else:                                               # 빨갛게 페인트 많이 되어있으면
                    ans += flag[i].count('W') + flag[i].count('B')  # 빨갛게 페인트
                    record[i] = 'R'
            else:                                               # 빨간색 페인트만 가능하면
                ans += flag[i].count('W') + flag[i].count('B')  # 빨간색 페인트
                record[i] = 'R'

        elif record[i-1] == 'W':                                # 하얀 or 파랑 페인트 가능
            if w >= b:                                          # 하얀 페인트 많이 되어있으면
                ans += flag[i].count('B') + flag[i].count('R')  # 하얗게 페인트하고
                record[i] = 'W'                                 # 색 기록 남김
            else:                                               # 파랑 페인트 많이 되어있으면
                ans += flag[i].count('W') + flag[i].count('R')  # 파랗게 페인트 하고
                record[i] = 'B'                                 # 색 기록 남김

        elif record[i-1] == 'B':                                # 파랑 or 빨강 페인트 가능
            if b >= r:                                          # 파랑 페인트 많이 되어있으면
                ans += flag[i].count('W') + flag[i].count('R')  # 파랗게 페인트 하고
                record[i] = 'B'                                 # 색 기록 남김
            else:                                               # 빨강 페인트 많이 되어있으면
                ans += flag[i].count('W') + flag[i].count('B')  # 빨갛게 페인트 하고
                record[i] = 'R'                                 # 색 기록 남김

        else:                                                   # 빨갛게만 페인트 가능하면
            ans += flag[i].count('W') + flag[i].count('B')      # 빨갛게 페인트 하고
            record[i] = 'R'                                     # 색 기록 남김
    print('#{} {}'.format(tc, ans))