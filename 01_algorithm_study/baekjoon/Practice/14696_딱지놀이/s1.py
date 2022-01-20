import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A_count = [0] * 4
    B_count = [0] * 4
    for i in range(1, len(A)):
        A_count[A[i]-1] += 1

    for i in range(1, len(B)):
        B_count[B[i]-1] += 1
    #
    # print(A_count)
    # print(B_count)
    result = 4
    while result:
        A_num = A_count.pop()
        B_num = B_count.pop()
        if A_num > B_num:
            print('A')
            result = False
        elif B_num > A_num:
            print('B')
            result = False
        elif result == 1:
            print('D')
            result = False
        else:
            result -= 1


