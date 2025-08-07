function solution(name) {
    // 1. 상하 / 좌우 작업을 따로 처리
    // 2. 상하 이동 횟수는 고정되어 있으니, 좌우에 집중
    // 3. 좌우 이동은 3가지 케이스 고려(왼쪽으로만 이동, 오른쪽으로만 이동, 중간에 꺽는 이동)
    let n = name.length;
    let moveUpDown = 0;
    
    // 상하 조작 횟수 계산
    for (let i = 0; i < n; i++) {
        if (name[i] === 'A') {
            continue;
        }
        const up = name.charCodeAt(i) - 'A'.charCodeAt(0);
        const down = 'Z'.charCodeAt(0) - name.charCodeAt(i) + 1;
        moveUpDown += Math.min(up, down);
    }
    
    // 좌우 조작 횟수 계산 - "ABAAABA"
    // 1. 오른쪽으로만 이동
    let minLRMove = n - 1;
    for (let i = 0; i < n; i++) {
        // 2. 연속하는 A가 어디까지 이어지는지 구한다
        let idxEndA = i + 1;
        while (idxEndA < n && name[idxEndA] === 'A') {
            idxEndA++;
        }
        
        // 3. 처음 -> 오른쪽(i) -> 처음 이동 (오른쪽 -> 왼쪽)
        const moveRightToLeft = i + i + (n - idxEndA);
        // 4. 처음 -> 왼쪽 -> 처음 이동 (왼쪽 -> 오른쪽)
        const moveLeftToRight = (n - idxEndA) * 2 + i;
        minLRMove = Math.min(minLRMove, moveRightToLeft, moveLeftToRight);
    }
    
    return moveUpDown + minLRMove;
}