import sys
sys.stdin = open("input.txt")

N = int(input())
candy = [list(map(str, input())) for _ in range(N)]
cnt = 0

def cnt_candy():
    global cnt
    for k in range(N):
        tmp = 1
        for l in range(1, N):
            if candy[k][l] == candy[k][l-1]:
                tmp += 1
            else:
                tmp = 1

            if tmp > cnt:
                cnt = tmp

        if cnt == N:
            return

        tmp = 1
        for m in range(1, N):
            if candy[m][k] == candy[m-1][k]:
                tmp += 1
            else:
                tmp = 1

            if tmp > cnt:
                cnt = tmp

        if cnt == N:
            return

for i in range(N):
    for j in range(N):
        if j+1 < N:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            cnt_candy()
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]

        if i+1 < N:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            cnt_candy()
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

print(cnt)