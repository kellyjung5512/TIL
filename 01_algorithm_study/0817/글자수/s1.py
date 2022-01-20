import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = list(map(str, input()))
    str2 = input()
    check = [0] * len(str1)
    for i in range(len(str2)):
        if str2[i] in str1:
            check[str1.index(str2[i])] += 1
    print('#{} {}'.format(tc, max(check)))

