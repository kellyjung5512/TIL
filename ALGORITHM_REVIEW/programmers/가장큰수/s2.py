# 왜 틀렸을까 시도해보기
# 결론은 Type이 int가 아니라 str으로 나와야해서 틀린 것이었다.

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
        return 0
    # print(answer)
    return answer

print(solution(numbers))