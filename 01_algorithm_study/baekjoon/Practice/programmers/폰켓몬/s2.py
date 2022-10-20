# 다른사람의 풀이 보면서 깨달은 점
# set을 쓰고 list를 만들어줄 필요가 없음

def solution(nums):
    answer = len(nums) // 2
    nums = set(nums)
    if len(nums) < answer:
        answer = len(nums)
    return answer