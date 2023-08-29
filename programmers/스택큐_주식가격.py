# 시간초과 코드
# 리스트 slice, 리스트 append 때문인듯..?
def solution(prices):
    result = []
    for i, price in enumerate(prices):
        second = 0
        for next in prices[i+1:]:
            if next >= price:
                second += 1
            else:
                second += 1
                break
        result.append(second)
    
    return result

# 통과
def solution(prices):
    result = [0 for i in range(len(prices))]
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            result[i] += 1
            if prices[j] < prices[i]:
                break
    return result
    