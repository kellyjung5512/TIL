import sys
sys.stdin = open("input.txt")

N = int(input())
check = {}
for _ in range(N):
    tmp = input()
    tmp_check = tmp[tmp.index(".") + 1:len(tmp)]
    if tmp_check in check:
        check[tmp_check] += 1
    else:
        check[tmp_check] = 1

check = sorted(check.items())
for name, times in check:
    print(name, times)