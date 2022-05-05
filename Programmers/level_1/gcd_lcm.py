# 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12940
# => 최대공약수/최소공배수 구하기; 유클리드 호제법
# 예시 풀이
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))
