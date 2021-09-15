import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    my_num = list(map(int, input().split()))
    num_list = []
    for i in range(n-1):

        check = list(str(my_num[i] * my_num[i+1]))
        # print(check)
        for j in range(len(check)-1):
            if int(check[j]) <= int(check[j+1]):
                num_list.append(my_num[i] * my_num[i+1])
    # print(my_num)
    num_list.sort()
    if num_list :
        print('#{0} {1}'.format(tc, num_list[-1]))
    else:
        print('#{0} {1}'.format(tc, -1))