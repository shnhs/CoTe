from collections import deque

def solution(s):
    answer = 0

    # 텍스트를 탐색할 큐 생성
    text_que = deque()
    flag = None # 첫 시도에서 Flag는 None

    # 주어진 텍스트를 하나씩 순회
    for i in s:

        if i == 'z': # z가 들어왔을 때
            text_que.appendleft(i) # 큐에 넣기
            if flag == None:
                flag = 'z' # 처음 큐에 들어왔다면 flag를 z로 변경
                continue
            elif flag == 'a': # 이전에 flag가 a라면
                text_que.pop() # 큐의 끝 값(a)를 팝하고
                answer += 1 # 정답 +1
                flag = 'z' # flag는 a로 변경
            elif flag == 'z': # 이전의 flag가 z라면
                text_que.pop() # 이전의 z는 팝한다.

        elif i =='a': # a가 들어올경우엔 z와 반대로 동작
            text_que.appendleft(i)
            if flag == None:
                flag = 'a'
                continue
            elif flag == 'z':
                text_que.pop()
                answer += 1
                flag = 'a'
            elif flag == 'a':
                text_que.pop()
        
        else: # a나 z가 아닌경우 무시해도 됨
            pass

    return answer

print(solution("zabzczxa"))