// * 배열에서 존재하지 않는 가장 작은 양의 정수 찾기
// * 해결 포인트: 중복, 음수, 0, 큰 수 범위 예외처리
// * 핵심 스킬: Set, filter 기반 positive 원소 추출
function solution(A) {
    const positiveSet = new Set(A.filter((a) => a > 0));
    for (let i = 1; i <= positiveSet.size + 1; i++) {
        if (!positiveSet.has(i)) {
            return i;
        }
    }
}
