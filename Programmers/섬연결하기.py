from itertools import combinations

def solution(n, costs):
    answer = 0

    # 3번째 인자로 정렬
    costs.sort(key=lambda x:x[2])

    # 섬갯수 - 1의 부분집합 생성
    # subset = list(combinations(costs, n-1))
    subset = []
    for i in range(n-1, len(costs)+1):
        temp = list(combinations(costs, i))
        subset.extend(temp)

    ans_list = []
    for x in range(len(subset)-1):
        temp = []
        ans = []
        for y in range(n-1):
            temp.extend(subset[x][y][0:2])
            ans.extend(subset[x][y][2:])

        target = set(temp)

        if len(target) == n:
            ans_list.append(sum(ans))

    print(target)
    answer = min(ans_list)

    return answer


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
print(solution(5, [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]]))
print(solution(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]))