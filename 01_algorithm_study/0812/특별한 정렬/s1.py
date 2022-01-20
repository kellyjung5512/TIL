import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort()
    # print(num_list)
    new_list = []
    for i in range(len(num_list) - len(num_list) // 2):
        new_list.append(num_list[-1 - i])
        new_list.append(num_list[0 + i])
        if len(new_list) == 10:
            break
    print('#{} '.format(tc), end='')
    print(*new_list)