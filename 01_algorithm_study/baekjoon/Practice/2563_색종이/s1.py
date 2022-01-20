import sys
sys.stdin = open('input.txt')

T = int(input())
board = [[0] * 100 for _ in range(100)]
# print(board)
for _ in range(T):
    x, y = map(int, input().split())
    # print(x, y)
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1

    cnt = 0
    for i in range(100):
        for j in range(100):
            if board[i][j] == 1:
                cnt += 1

print(cnt)

