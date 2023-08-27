def permutation(arr, r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))] # 경우의 수를 만드는데 사용했는지 기록하는 리스트
    result = []
    
    def generate(chosen, used):
        if len(chosen) == r: # 만들고자 하는 개수가 되면 종료
            case = chosen.copy() # chosen은 경우의 수가 완성될 때마다 pop으로 초기화되므로, 해당 값을 저장하기 위해선 copy로 복사해줘야 함
            result.append(case)
            return
        
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i]) # 사용하지 않은 값이면 추가
                used[i] = 1 # 사용 기록
                generate(chosen, used) # 추가적으로 다음 값 추가를 위한 재귀함수 실행
                used[i] = 0 # 재귀함수를 다 돌며 하나의 경우의 수를 다 만들었다면, 사용 초기화
                chosen.pop() # chosen에서도 값을 비워주기
                
    generate([], used)
    return result

def get_result(case, k):
    count = 0
    for c in case:
        min_feat, used_feat = c[0], c[1]
        if k >= min_feat:
            k -= used_feat
            count += 1
        
    return count

def solution(k, dungeons):
    result = 0
    perm = permutation(dungeons, len(dungeons)) # 던전 순서 경우의 수 계산(순열 라이브러리 안쓰고 구현하기)
    
    # 경우의 수를 하나씩 돌면서 result를 갱신해 나감(던전 들어갈 수 있는지 + 들어간 후 결과 갱신에 대한 함수 별도 구현하기)
    for idx, case in enumerate(perm):
        count = get_result(case, k)
        if count > result:
            result = count
        
    return result