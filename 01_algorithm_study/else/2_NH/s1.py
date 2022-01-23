import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    students = [tuple(map(int, input().split())) for _ in range(N)]
    check = {}
    for student in students:
        if student in check:
            check[student] += 1
        else:
            check[student] = 1
    cnt = 0
    for value in check.values():
        if value > 1:
            cnt += value - 1
    print(cnt)