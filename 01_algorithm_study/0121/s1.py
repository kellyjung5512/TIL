import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    temp = list(input())
    # print(temp)
    for i in range(len(temp)):
        print(chr(2))