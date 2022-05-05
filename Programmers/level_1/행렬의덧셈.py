# 문제링크 : https://programmers.co.kr/learn/courses/30/lessons/12950

# 내 풀이
def solution(arr1, arr2):
    answer = []
    for x, y in zip(arr1,arr2):
        answer.append([a + b for a, b in zip(x,y)])
    return answer


def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer
  

def sumMatrix(A,B):
    return [list(map(sum, zip(*x))) for x in zip(A, B)]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))
