

def tictok(que):
    '''
    큐의 요소를 +1하는 함수
    '''
    for i in range(len(que)):
        que[i] += 1

    return que

def solution(bridge_length, weight, truck_weights):
    
    time = 0
    bridge_que = deque()
    truck_time_que = deque()
    
    while(True):
        # 현재 다리에 올라온거랑 다음트럭이 무게보다 가벼우면 트럭입성
        if sum(bridge_que) + truck_weights[0] < weight:
            bridge_que.appendleft(truck_weights[0])
            truck_time_que.appendleft(0)
            time += 1
        else: # 무게때문에 다음트럭이 못올라옴
            truck_time_que = tictok(truck_time_que) # 트럭 입성큐 +1
            time +=1

        # 트럭이 다리를 다 건넜다면
        if truck_time_que[-1] == bridge_length:
            bridge_que.pop()
            truck_time_que.pop()
        
        if not (truck_weights and bridge_que):
            break 

    return time

from collections import deque
print(solution(2,10,[7,4,5,6]))