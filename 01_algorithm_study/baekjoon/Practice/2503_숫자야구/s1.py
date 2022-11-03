import sys
sys.stdin = open("input.txt")
from itertools import permutations

N = int(input())
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
nums = list(permutations(nums, 3))
cnt = 0
for tc in range(N):
    answer, S, B = map(int, input().split())
    answer = list(str(answer))
    cnt = 0
    for i in range(len(nums)):
        strike = ball = 0
         i -= cnt
           for j in range(3):
              if nums[i][j] == answer[j]:
                strike += 1
            elif answer[j] in nums[i]:
                ball += 1

         if strike != S or ball != B:
              nums.remove(nums[i])
            cnt += 1

print(len(nums))