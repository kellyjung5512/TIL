# 딕셔너리 말고 방법 있나?

import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
dic = {arr2[i]: i for i in range(len(arr2))}

for i in arr:
    print(dic[i], end = ' ')