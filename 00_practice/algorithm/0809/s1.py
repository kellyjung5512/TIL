import sys
sys.stdin = open('input.txt')

N = int(input())
for _ in range(N):
    tmp = 0 # 체크하기
    res = 0 # 결과 도출
    check_list = [0] * 10
    card_list = list(map(int, input()))
    for a in card_list:
        check_list[a] += 1

    while tmp < 10:
        if check_list[tmp] >= 3:
            check_list[tmp] -= 3
            res += 1
        if check_list[tmp] >= 1 and check_list[tmp+1] >= 1 and check_list[tmp+2] >= 1:
            check_list[tmp] -= 1
            check_list[tmp + 1] -= 1
            check_list[tmp + 2] -= 1
            res += 1
        tmp += 1
    if res == 2:
        print('yes')
    else:
        print('no')