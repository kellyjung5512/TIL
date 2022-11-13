import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    nums = list(map(int, input()))
    check_list = [0] * 10
    for num in nums:
        check_list[num] += 1
    max_num = max(check_list)
    for i in range(len(check_list) - 1, 0, -1):
        if check_list[i] == max_num:
            print(i, check_list[i])
            break