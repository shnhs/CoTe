def solution(waiting):
    answer = []

    reserved = {}
    # 예약완료되었다면 딕셔너리로 옮기기
    for i in waiting:
        if not (i in reserved.keys()):
            reserved[i] = 1
    
    return list(reserved.keys())


print(solution([1, 5, 8, 2, 10, 5, 4, 6, 4, 8]))