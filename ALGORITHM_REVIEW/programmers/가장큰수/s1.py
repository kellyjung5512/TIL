import itertools
def solution(numbers):
    answer = ''
    result = []
    if len(numbers) > 0:
        # check = [i for i in range(len(numbers))]
        check_ans = list(itertools.permutations(numbers))
        # print(check_ans)
        for i in range(len(check_ans)):
            temp = ''
            for j in range(len(check_ans[i])):
                temp += str(check_ans[i][j])
            # print(temp)
            if temp > answer:
                answer = temp
    else:
        return answer
    # result = list(map(int, result))
    # result.sort(reverse=True)
    # # answer = str(result[0])
    # answer = result[0]
    return answer