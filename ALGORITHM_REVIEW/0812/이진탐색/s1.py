import sys
sys.stdin = open('input.txt')

def search(student):
    cnt = 0
    start = 1
    end = P
    while start < end:
        middle = (start + end) // 2
        if middle == student:
            cnt += 1
            return cnt
        elif middle < student:
            start = middle
            cnt += 1
        elif middle > student:
            end = middle
            cnt += 1

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    student_A = search(A)
    student_B = search(B)


    if student_A < student_B:
        print('#{} {}'.format(tc, 'A'))
    elif student_A > student_B:
        print('#{} {}'.format(tc, 'B'))
    else:
        print('#{} {}'.format(tc, 0))
