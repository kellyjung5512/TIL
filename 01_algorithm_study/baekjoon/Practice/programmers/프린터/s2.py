# 말 그대로 확인 후 다시 넣기
# max() 함수를 이렇게 쓸 수 있는 줄 몰랐다...!
# max값을 찾을 때는 튜플 내에 있는 원소 0번째에 비교할 값을 넣는게 맞음 (중요!)

def solution(priorities, location):
    answer = 0

    queue = [(idx, num) for (num, idx) in enumerate(priorities)]

    while len(queue):
        item = queue.pop(0)
        if queue and max(queue)[0] > item[0]:
            queue.append(item)
        else:
            answer += 1
            if item[1] == location:
                break

    return answer

solution([2, 1, 3, 2], 2)