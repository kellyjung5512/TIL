# 맞긴 한데 재귀가 너무 큰지 런타임에러 & 시간 초과가 뜸

def solution(n):
    answer = 0
    def fibo(num):
        if num > 1:
            return fibo(num - 1) + fibo(num - 2)
        else:
            return num
    answer = fibo(n) % 1234567
    return answer