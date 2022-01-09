# 정답
numbers = [0, 0, 0]

def solution(numbers):
    answer = ''
    result = []
    new_numbers = []
    for i in numbers:
        new_numbers.append((str(i) * 3, i))
    new_numbers.sort(key = lambda x: x[0], reverse = True)
    for _, temp in new_numbers:
        answer += str(temp)
    if answer[0] == '0':
        answer = '0'
    # print(answer)
    return answer

print(solution(numbers))