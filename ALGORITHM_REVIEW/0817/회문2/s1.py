import sys
sys.stdin = open('input.txt')

# for tc in range(1, 11):
#     T = int(input())
#     palindrome = [list(map(str, input())) for _ in range(100)]
#     # print(palindrome)
#     num = 0
#     for i in range(100):
#         for j in range(99, -1, -1):
#             cnt = 0
#             check = palindrome[i][i:j]
#             for k in range(len(check)//2):
#                 if check[k] == check[-1-k]:
#                     cnt += 1
#                 else:
#                     break
#             if cnt == len(check)//2 and num < len(check):
#                 num = len(check)
#                 break
#
#     print(num)

