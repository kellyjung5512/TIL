def solution(citations):
    answer = 0
    max_c = max(citations)
    citations.sort(reverse=True)
    for i in range(max_c, 0, -1):
        result = 0
        for c in citations:
            if c >= i:
                result += 1
        if result >= i:
            answer = i
            break

    return answer