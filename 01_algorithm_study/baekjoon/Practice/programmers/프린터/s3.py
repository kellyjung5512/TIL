# 처음 작성한 풀이 다시 수정해보기
# enumerate 적응됐다 ^__^!!

def solution(priorities, location):
    answer = 0
    make_list = []

    for idx, num in enumerate(priorities):
        make_list.append((num, idx))

    while len(priorities) > 0:
        max_num = max(make_list)[0]
        tmp_num, tmp_idx = make_list.pop(0)
        if max_num > tmp_num and make_list:
            make_list.append((tmp_num, tmp_idx))
        else:
            answer += 1
            if tmp_idx == location:
                break

    return answer

print(solution([2, 1, 3, 2], 2))