import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num, change = map(str, input().split())
    change_num = int(change)
    num_list = list(map(int, num))

    min_num = num_list[0]
    min_num_idx = 0
    max_num = num_list[0]
    max_num_idx = 0

    cnt = 0
    while cnt < change_num:
        for i in range(1, len(num_list)):
            if num_list[i] >= max_num:
                max_num_idx = i
                max_num = num_list[i]
            if num_list[i] <= min_num:
                min_num_idx = i
                min_num = num_list[i]
        num_list[max_num_idx] = min_num
        num_list[min_num_idx] = max_num
        cnt += 1
    print(num_list)