import sys
sys.stdin = open('input.txt')

def search(b, t):
    b_list = set()
    t_list = set()

    for i in range(len(binary)):
        temp = binary[:]
        if temp[i] == '1':
            temp[i] = '0'
        else:
            temp[i] = '1'
        num = ''.join(map(str, temp))
        b_list.add(int(num, 2))

    for j in range(len(ternary)):
        ternary_list = {'0', '1', '2'} - set(ternary[j])
        temp = ternary[:]
        for k in ternary_list:
            temp[j] = k
            num = ''.join(map(str, temp))
            t_list.add(int(num, 3))

    return b_list & t_list

T = int(input())
for tc in range(1, T+1):
    binary = list(input())
    ternary = list(input())
    result = search(binary, ternary)
    print('#{} {}'.format(tc, result.pop()))
    # print('#{} {}'.format(tc, *result))