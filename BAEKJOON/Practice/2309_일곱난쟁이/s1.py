import sys
sys.stdin = open('input.txt')

height = [int(input()) for i in range(9)]
total_height = sum(height)
height.sort()

for i in range(len(height)-1):
    for j in range(1, len(height)):
        if total_height - height[i] - height[j] == 100 and i != j:
            result = [height[i], height[j]]
# print(result)
for i in result:
    height.remove(i)

for i in range(len(height)):
    print(height[i])