import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    new_arr = list(zip(*arr[::-1]))
    new_arr2 = list(zip(*new_arr[::-1]))
    new_arr3 = list(zip(*new_arr2[::-1]))
    print('#{}'.format(tc))
    for i in range(len(arr)):
        ans = []
        temp1 = ''
        temp2 = ''
        temp3 = ''
        for j in range(len(arr[i])):
            temp1 += str(new_arr[i][j])
            temp2 += str(new_arr2[i][j])
            temp3 += str(new_arr3[i][j])
        ans = [temp1, temp2, temp3]
        print(*ans)