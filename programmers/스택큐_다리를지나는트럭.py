# bridge_length => 다리 길이, 1칸 지나갈 때마다 1초 
# 다리길이 옵션에 맞게 코드 수정해야 함
def solution(bridge_length, weight, truck_weights):
    bridge_list = [] # 다리를 건너는 트럭
    bridge_sum = 0 # 다리 무게 합계
    spend_time = 0 # 소요된 시간
    
    while True:
        if spend_time > 0 and bridge_sum == 0: 
            break
            
        # 다리를 건너는 트럭 수가 꽉 찬 경우
        if len(bridge_list) > bridge_length - 1:
            bridge_sum -= bridge_list[0]
            bridge_list.pop(0)
            
        # 아직 다리를 건너지 않은 트럭이 남아있는 경우
        if len(truck_weights) != 0:
            if bridge_sum + truck_weights[0] <= weight:
                bridge_list.append(truck_weights.pop(0))
                bridge_sum += bridge_list[-1]
            else:
                bridge_list.append(0) # 비어있는 1초를 세기 위해 의미없는 값 추가
        else:
            bridge_list.append(0) # 비어있는 1초를 세기 위해 의미없는 값 추가
        spend_time += 1

    return spend_time