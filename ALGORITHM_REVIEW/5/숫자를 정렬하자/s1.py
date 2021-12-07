import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num = int(input())
    temp = list(map(int, input().split()))
    temp.sort()
    print('#{} '.format(tc), end='')
    print(*temp)