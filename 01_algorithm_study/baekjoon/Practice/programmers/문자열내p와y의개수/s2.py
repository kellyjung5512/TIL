# 새로 푼 코드
# lower나 count같은 함수를 좀 더 잘 사용하면 좋겠다는 생각이 들었다.

def solution(s):
    answer = False
    if s.lower().count("p") == s.lower().count("y"):
        answer = True
    return answer