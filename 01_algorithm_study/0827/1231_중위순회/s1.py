import sys
sys.stdin = open('input.txt')

def in_order(num):
    global ans
    if num:
        in_order(left[num])
        # print(words[num], end='')
        ans += words[num]
        in_order(right[num])
    return ans

for tc in range(1, 11):
    N = int(input())
    words = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    ans = ''

    for _ in range(N):
        temp = list(map(str, input().split()))
        try:
            for i in range(4):
                words[int(temp[0])] = temp[1]
                left[int(temp[0])] = int(temp[2])
                right[int(temp[0])] = int(temp[3])
        except:
            continue


    print('#{} {}'.format(tc, in_order(1)))
