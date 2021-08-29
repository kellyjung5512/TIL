import sys
sys.stdin = open('input.txt')

num = int(input())
max_cnt = [0, 0]
if num > 0:
    for i in range(0, num+1):
        check_list = [num]
        check_list.append(num-i)
        idx = 1

        while idx != 0:
            if check_list[idx-1] - check_list[idx] >= 0:
                check_list.append(check_list[idx-1] - check_list[idx])
                idx += 1
            else:
                idx = 0
        if max_cnt[1] <= len(check_list):
            max_cnt = [i, len(check_list)]
    #     print(check_list)
    # print(max_cnt)

    check_list = [num, num-max_cnt[0]]
    idx = 1
    while idx != 0:
        if check_list[idx - 1] - check_list[idx] >= 0:
            check_list.append(check_list[idx - 1] - check_list[idx])
            idx += 1
        else:
            idx = 0
    print(max_cnt[1])
    print(*check_list)
else:
    print(0)

