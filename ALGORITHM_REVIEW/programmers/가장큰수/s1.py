import itertools
def solution(numbers):
    answer = ''
    result = []
    if len(numbers) > 0:
        # check = [i for i in range(len(numbers))]
        check_ans = list(itertools.permutations(numbers))
        for i in range(len(check_ans)):
            temp = ''
            for j in range(len(check_ans[i])):
                temp += str(check_ans[i][j])
            if temp > answer:
                answer = temp
    else:
        return answer

    return answer