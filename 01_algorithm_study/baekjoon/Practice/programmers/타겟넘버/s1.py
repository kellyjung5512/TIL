def solution(numbers, target):
    total = 0

    def dfs(n, sum_num):
        nonlocal total
        # print(n, len(numbers), sum_num, target, total)
        if n == len(numbers):
            if sum_num == target:
                total += 1
            return
        else:
            dfs(n + 1, sum_num + numbers[n])
            dfs(n + 1, sum_num - numbers[n])
        return total

    answer = dfs(0, 0)
    return answer