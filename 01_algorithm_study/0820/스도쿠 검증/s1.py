import sys
sys.stdin = open('input.txt')

def check_sudoku(arr):
    for i in range(9):
        check = [0] * 9
        for j in range(9):
            check[arr[i][j] - 1] += 1
            check[arr[j][i] - 1] += 1
        if 1 in check:
            return 0

    for i in range(0, len(arr),3):
        check = [0] * 9
        for j in range(0, len(arr), 3):
            for k in range(0, 3):
                for l in range(0, 3):
                    check[arr[i + k][j + l] - 1] += 1
            if 0 in check:
               return 0

    return 1

T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    ans = check_sudoku(sudoku)

    print('#{} {}'.format(tc, ans))