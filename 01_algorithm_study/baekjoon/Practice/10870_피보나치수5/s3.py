import sys
sys.stdin = open("input.txt")

def fibo(a):
    if a <= 1:
        return a
    return fibo(a-1) + fibo(a-2)

n = int(input())
print(fibo(n))