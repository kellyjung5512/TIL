import sys
sys.stdin = open('input.txt')

N = int(input())
pick_list = list(map(int, input().split()))
student = [i for i in range(1,N+1)]
print(pick_list)
print(student)

for i in range(len(pick_list))