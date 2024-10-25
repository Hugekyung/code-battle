#문제 설명#
#숫자 배열 하나를 입력받아 가능한 부분 배열 각각의 합을 계산하고, 합이 가장 큰 부분 배열을 반환하는 함수를 작성하시오.
#입력 예시
# [3, -1, 4, -2, 5]
#출력 예시
#'가장 합이 큰 조합은 (3, 4, 5)이고, 그 합은 12'

from itertools import combinations

def find_max_combi(array):
    max_sum = float('-inf')
    max_combi = None

    # 모든 가능한 조합을 탐색
    for r in range(1, len(array) + 1):
        combi_arr = list(combinations(array, r))
        for combi in combi_arr:
            sum_combi = sum(list(combi))
            if sum_combi > max_sum:
                max_sum = sum_combi
                max_combi = combi

    return max_combi

# 입력 배열
input_arr = [3, -1, 4, -2, 5]
my_max_combi = find_max_combi(input_arr)

# 함수 호출 및 결과 출력
print(f"가장 합이 큰 조합은 {my_max_combi}이고, 그 합은 {sum(my_max_combi)}")
