import sys
sys.stdin = open('input.txt')
from itertools import combinations_with_replacement

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [1, 2, 3]
    new_arr = list(combinations_with_replacement(arr, n))
    for i in range(len(new_arr)):
        if sum(new_arr[i]) == n:
            print("yes")
    print(new_arr)