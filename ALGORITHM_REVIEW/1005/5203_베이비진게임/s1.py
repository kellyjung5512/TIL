import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))

    A_check = [0] * 10
    B_check = [0] * 10
    ans = 0   # 1 A 이긴거 2 B 이긴거 0 무승부

    for j in range(6):
        A_check[cards[2 * j]] += 1
        B_check[cards[2 * j + 1]] += 1
        if j >= 2:
            for k in range(8):
                if A_check[k] >= 1 and A_check[k+1] >= 1 and A_check[k+2] >= 1:  # 시발 순서
                    ans = 1
                    break
                if B_check[k] >= 1 and B_check[k+1] >= 1 and B_check[k+2] >= 1:
                    ans = 2
                    # break
            if ans != 1:    # ans != 0
                for k in range(10):
                    if A_check[k] >= 3:
                        ans = 1
                        break
                    if B_check[k] >= 3:
                        ans = 2
                    # break
            else:
                break

        if ans != 0:
            break
    print('#{} {}'.format(tc, ans))