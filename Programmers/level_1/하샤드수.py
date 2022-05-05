# 문제링크; https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
  # 숫자의 각 자리수의 합을 구하기 
  # => 무언가 반복되는 객체를 다루는경우에 map을 생각하는 습관!
  if x % sum(map(int, str(x))) == 0:
    return True
  else:
    return False
  
print(solution(13))
