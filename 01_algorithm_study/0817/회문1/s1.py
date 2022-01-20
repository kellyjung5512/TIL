import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    num = int(input())
    palindrome = [list(map(str, input())) for _ in range(8)]

    res = 0
    for i in range(8):
        for j in range(8 - num + 1):
            check2 = ''
            check1 = palindrome[i][j:j+num]
            for l in range(j, j+num):
                check2 += palindrome[l][i]
            cnt1, cnt2 = 0, 0
            for k in range(num//2):
                if check1[k] == check1[-1-k]:
                    cnt1 += 1
                if check2[k] == check2[-1-k]:
                    cnt2 += 1
            if cnt1 == num//2:
                res += 1
            if cnt2 == num//2:
                res += 1

    print('#{} {}'.format(tc, res))