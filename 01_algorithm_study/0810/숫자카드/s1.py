import sys
sys.stdin = open('input.txt')

def find_card(find_num):
    for i in range(9, -1, -1):
        if check[i] == find_num:
            return i

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))
    check = [0] * 10
    for card in cards:
        check[card] += 1
    ans = find_card(max(check))
    how_many = check[ans]

    print('#{} {} {}'.format(tc, ans, how_many))

