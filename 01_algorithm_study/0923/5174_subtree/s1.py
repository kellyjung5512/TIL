import sys
sys.stdin = open('input.txt')

def is_order(num):
    global ans
    if num:
        is_order(left[num])
        is_order(right[num])
        ans += 1
    return ans

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    node = list(map(int, input().split()))
    V = E + 1
    left = [0] * (V + 1)
    right = [0] * (V + 1)
    ans = 0

    for i in range(0, len(node), 2):
        if left[node[i]] == 0:
            left[node[i]] = node[i+1]
        else:
            right[node[i]] = node[i+1]

    print('#{} {}'.format(tc, is_order(N)))