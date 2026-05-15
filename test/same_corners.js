// 3번 문제 - same_corners
function solution(A) {
    // 시작과 끝이 같은 숫자인 최소 2개 이상 연속하는 배열의 값을 추출한 것 중 합이 가장 큰 경우의 수
    let maxValue = -1;
    const lastIndexMap = new Map();
    for (let i = 0; i < A.length; i++) {
        lastIndexMap.set(A[i], i); // 각 값의 가장 마지막 값 해시 저장
    }
    // 각 원소의 위치에서 가장 멀리 떨어진 자신과 같은 정수가 있는지 탐색
    // 있으면 현재 위치의 정수 ~ 찾은 위치까지의 값들을 slice해서 합을 구하고 max 업데이트
    for (let i = 0; i < A.length; i++) {
        const sameValueIdx = lastIndexMap.get(A[i]);
        if (sameValueIdx <= i) {
            continue; // 길이가 2개가 안되면 continue;
        }
        const newArr = A.slice(i, sameValueIdx + 1);
        const sumArr = newArr.reduce((acc, curr) => acc + curr, 0);
        maxValue = Math.max(maxValue, sumArr);
    }
    return maxValue;
}
