import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    num = int(input())
    my_list = [list(map(int, input().split())) for _ in range(num)]
    cnt = 0
    for i in range(num):
        check_list = []
        for j in range(num):
            if my_list[j][i] == 1:
                check_list.append(1)
            if my_list[j][i] == 2:
                if check_list:
                    check_list = []
                    cnt += 1
                else:
                    pass
            else:
                pass
    print('#{0} {1}'.format(tc, cnt))