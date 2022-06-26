import sys
sys.stdin = open('input.txt')

N = int(input())
number_list = list(map(int, input().split()))
prime_number = 0

for number in number_list:
    cnt = 0
    if number > 1:
        for i in range(2, number+1):
            if (number % i == 0):
                cnt += 1
    if (cnt == 1):
        prime_number += 1

print(prime_number)