# 두번째 풀이
# 프로그래머스 질문하기 보고 해결
# 솔직히 첫번째 풀이처럼 for문을 2번 돌릴 필요 조차 없다는 것을 깨달음
# sort해서 앞뒤만 비교하면 될 일이었음
# 효율성 테스트도 완벽하게 통과함
# 레벨 2에서도 헤매고 있으니 조금은 답답함

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True
