# 프로그래머스 스킬체크 문제 - level3 - 문제 제목 없음
from collections import defaultdict

def solution(genres, plays):
    # 재생횟수가 많은 순으로 장르 순서 맞추기
    dict = defaultdict(int)
    for g, p in zip(genres, plays):
        dict[g] += p
    sorted_arr = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    
    # 장르별 재생횟수가 많은 순으로 해당 key에 value값으로 추가
    dict_new = { g : [] for g, _ in sorted_arr}
    for i in range(len(genres)):
        g, p = genres[i], plays[i]
        dict_new[g].append((i, p))
    
    result = []
    for k, v in dict_new.items():
        if len(v) == 1:
            result.append(v[0][0])
            continue
        # 조건 3: 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
        sorted_v = sorted(v, key=lambda x: (x[1], -x[0]))
        result.append(sorted_v.pop()[0])
        result.append(sorted_v.pop()[0])
    return result