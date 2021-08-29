import sys
sys.stdin = open('input.txt')

T = int(input())
paper = [[0] * 101 for _ in range(101)]

for i in range(1, T+1):
    x1, y1, width, height = map(int, input().split())
    for x in range(width):
        for y in range(height):
            paper[x1+x][y1+y] = i

for i in range(1, T+1):
    cnt = 0
    for x in range(101):
        for y in range(101):
            if paper[x][y] == i:
                cnt += 1
    print(cnt)
