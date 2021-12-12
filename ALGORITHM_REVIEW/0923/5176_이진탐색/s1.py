import sys
sys.stdin = open('input.txt')

def binary_tree(num):
    global ans
    if num <= N:
        binary_tree(num * 2)
        tree[num] = ans
        ans += 1
        binary_tree(num * 2 + 1)
        return tree


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)
    ans = 1
    binary_tree(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N // 2]))