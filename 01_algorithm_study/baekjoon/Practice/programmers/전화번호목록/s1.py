# 첫번째로 푼 풀이
# 솔직히 틀린건 아닌 것 같은데 효율성에서 Zero
# 다음 단계로 안넘어감.. 답답
# 왜일까 계속 고민 (약 30분)

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False
    return True