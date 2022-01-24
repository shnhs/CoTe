from collections import deque

def tictok(que):
    '''
    큐의 요소를 +1하는 함수
    '''
    for i in range(len(que)):
        que[i] += 1

    return que

def solution(bridge_length, weight, truck_weights):
    
    T = len(truck_weights)
    time = 0
    bridge_que = deque()
    truck_time_que = deque()
    passed_truck = deque()
    
    while(True):
        # 일단 대기트럭이 있을때
        if truck_weights:
            # 현재 다리에 올라온거 + 다음트럭이 한계무게보다 무겁지 않으면
            if sum(bridge_que) + truck_weights[0] <= weight:
                time += 1
                bridge_que.appendleft(truck_weights.pop(0)) # 트럭입성
                truck_time_que.appendleft(0)
                truck_time_que = tictok(truck_time_que) # 트럭 입성큐 +1 
            else: # 무게가 넘친다면 다음트럭이 못올라옴
                time +=1
                truck_time_que = tictok(truck_time_que) # 트럭 입성큐 +1

        # 대기트럭이 없을 때
        elif (not truck_weights) and bridge_que:
            time +=1
            truck_time_que = tictok(truck_time_que) # 트럭 입성큐 +1

        # 끝에 트럭이 다리를 다 건넜다면
        if truck_time_que[-1] == bridge_length:
            passed_truck.appendleft(bridge_que.pop())
            truck_time_que.pop()
        
        # 모든 트럭이 다리를 다 건넜다면
        if len(passed_truck) == T:
            break

    return time+1

print(solution(2,10,[7,4,5,6]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))