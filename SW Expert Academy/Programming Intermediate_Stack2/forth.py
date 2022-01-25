
n = open("SW Expert Academy\Programming Intermediate_Stack2\input.txt", "r")

T = int(n.readline())

# 계산기 함수
def calc(A, B, op):
    if(op == '+'):
        return A+B
    elif(op == '-'): 
        return A-B
    elif(op == '*'): 
        return A*B
    elif(op == '/'): 
        return int(A/B)

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = n.readline().split()  # 수식 입력 받기
    
    cal_stack = []
    # 문자열에서 하나씩 반복
    for x in N:
        if x.isdecimal(): # 꺼낸 문자가 숫자라면
            cal_stack.append(int(x)) # 스택에 숫자 추가
        elif x == '.': # .이 입력됬다면
            if len(cal_stack) == 1:
                ans = cal_stack.pop() # 계산 결과를 출력하자
            else:
                ans = 'error'
                break
        else: # 꺼낸 문자가 연산 기호라면
            try:
                A = cal_stack.pop()
                B = cal_stack.pop()
                temp = calc(B, A, x) # 계산 수행; 나눗셈 때문에 순서 주의!
                cal_stack.append(temp)
            except:
                ans = 'error'
                break

    print(f'#{test_case} {ans}')