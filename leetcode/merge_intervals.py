class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 구간 시작점 기준으로 오름차순 정렬 후, 이전 구간의 끝과 현재 구간의 시작이 겹치는지 확인
        intervals.sort()
        print(intervals)
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            st, en = intervals[i]
            prev_st, prev_en = res[-1]
            if prev_en >= st:
                res.pop()
                res.append([prev_st, max(en, prev_en)])
                continue
            res.append(intervals[i])

        return res