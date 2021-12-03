import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input()))
    check = [0] * 10
    cnt = 0
    for card in cards:
        check[card] += 1
    # print(check)
    idx = 0
    while idx < len(check):
        if check[idx] >= 3:
            cnt += 1
            check[idx] -= 3
            continue
        if idx < len(check) - 2:
            if check[idx] and check[idx+1] and check[idx+2]:
                cnt += 1
                check[idx] -= 1
                check[idx+1] -= 1
                check[idx+2] -= 1
                continue
        if cnt == 2:
            print('#{} 1'.format(tc))
            break
        idx += 1

    else:
        print('#{} 0'.format(tc))
