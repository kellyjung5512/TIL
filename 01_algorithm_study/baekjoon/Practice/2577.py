# a = int(input())
# b = int(input())
# c = int(input())

a=150
b=266
c=427

# result = ''
# result = str(a * b * c)
# result_list = [0,0,0,0,0,0,0,0,0,0]
# for i in result :
#     i = int(i)
#     result_list[i] += 1 
# result = map(str, result_list)
# print(result)


a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))
print(result)
for i in range(10):
    print(result.count(str(i)))