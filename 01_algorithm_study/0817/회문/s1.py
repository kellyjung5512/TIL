import sys
sys.stdin = open('input.txt')

def find_palindrome(palindrome):
    for i in range(N):
        for j in range(N-M+1):
            check = palindrome[i][j:j + M]
            if check == check[::-1]:
                return check

    for i in range(N-M+1):
        for j in range(N):
            check = ''
            for k in range(M):
                check += palindrome[k+i][j]
            if check == check[::-1]:
                return check

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    palindrome = [input() for _ in range(N)]
    # find_palindrome(palindrome)

    print('#{} {}'.format(tc, find_palindrome(palindrome)))