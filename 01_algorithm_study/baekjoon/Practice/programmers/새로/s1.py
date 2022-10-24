# 처음 작성한 풀이
# 완전 노가다 풀이라고 생각됨. 통과 되지 못한 코드
# 코드 짜면서도 통과 안될거라고 생각했다.. 새로운 코드 생각해보자

def solution(priorities, location):
    answer = 0
    make_list = []
    time = 1

    for idx, num in enumerate(priorities):
        make_list.append((num, idx))

    while len(priorities) > 0:
        max_num = 0
        idx_num = 0
        for idx, num in make_list:
            if max_num < num:
                max_num = num
                idx_num = idx
        make_list = make_list[idx_num:] + make_list[:idx_num]
        tmp_num, tmp_idx = make_list.pop(0)
        if tmp_idx == location:
            answer = time
            break
        else:
            time += 1
    return answer