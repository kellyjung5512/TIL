import sys
sys.stdin = open("input.txt")

N = int(input())
res = 0
for _ in range(N):
    strs = list(map(str, input()))
    check_list = []
    tmp = True
    for i in range(len(strs)):
        if strs[i] not in check_list:
            check_list.append(strs[i])
        else:
            if strs[i] == check_list[-1]:
                pass
            else:
                tmp = False
                break
    if tmp == True:
        res += 1
print(res)