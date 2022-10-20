# set을 오랜만에 다시 생각해보게 된 계기
# sort, set 잊지말자..!

def solution(nums):
    answer = len(nums) // 2
    nums = list(set(nums))
    if len(nums) < answer:
        answer = len(nums)
    return answer