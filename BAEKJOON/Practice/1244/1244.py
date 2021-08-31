import sys
sys.stdin = open('input.txt')

def number_switch(n):
    if switch[n] == 0:
        switch[n] = 1
    else:
        switch[n] = 0
    return

n = int(input())
switch_list = list(map(int, input().split()))

students = int(input())
for student in range(students):
    sex, switch = map(int, input().split())
    if sex == 1:
        idx = switch
        for i in range(2, 100):
            while idx <= len(switch_list):
                number_switch(idx) 
                idx = idx * i

    if sex == 2 :
        idx = switch-1
        for i in range(1,n//2):
            if switch + i > n or switch - i < 1 :
                break
            if switch_list[idx-i] == switch_list[idx+i]:
                number_switch(idx-i)
                number_switch(idx+i)
    
    print(switch_list)
    # print(switch_list)
