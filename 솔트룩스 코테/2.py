def solution(arr, n):
    answer = False

    arr = set(arr)

    for i in arr:
        if (n%2 == 0) and (int(n/2)==i):
            continue
        if n-i in arr:
            answer = True
            break

    return answer

print(solution([5, 3, 9, 13], 8))