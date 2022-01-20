cnt = int(input())
numbers = []
for i in range(cnt) :
    numbers.append(int(input()))

numbers.sort()
for i in numbers :
    print(i)