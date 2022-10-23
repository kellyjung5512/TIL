def solution(arr):
    answer = [arr[0]]
    stack = []
    for num in arr:
        if num == answer[-1]:
            pass
        else:
            answer.append(num)
    return answer