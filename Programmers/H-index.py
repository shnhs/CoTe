def solution(citations):
    answer = 0
    
    # 논문길이
    n = len(citations) 

    # 논문길이 큰 수 부터 반복
    for i in range(n, 0, -1):
        cnt = 0
        # 논문의 인용횟수가 해당 수보다 크면
        for x in citations:
            if x >= i:
                cnt += 1 # 카운트 +1

        # 카운트가 h보다 크면 답안으로
        if cnt >= i:
            answer = i
            break

    return answer

print(solution([3, 0, 6, 1, 5]))