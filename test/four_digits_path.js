// 1번 문제 - four_digits_path
function bfs(board, n, m, s, t) {
    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];
    const queue = [];
    const initNumStr = String(board[s][t]);
    const initVisited = new Set([`${s},${t}`]) // 문자열 처리
    queue.push([s, t, initNumStr, initVisited]);

    let maxNum = 0;
    while (queue.length > 0) {
        const [x, y, numStr, visited] = queue.shift();
        if (numStr.length === 4) {
            maxNum = Math.max(maxNum, Number(numStr));
            continue;
        }

        for (let i = 0; i < 4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];
            if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
                continue;
            }

            const next = `${nx},${ny}`;
            if (!visited.has(next)) {
                const nextNumStr = numStr + String(board[nx][ny]);
                const nextVisited = new Set(visited);
                nextVisited.add(next);
                queue.push([nx, ny, nextNumStr, nextVisited]);
            }
        }
    }
    return maxNum;
}

function solution(Board) {
    // 시작 지점에서 인접한 칸으로 이동하는 경우의수를 따져봤을 때 가장 큰 네 자리 정수 반환
    const n = Board.length;
    const m = Board[0].length;
    let maxValue = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            maxValue = Math.max(maxValue, bfs(Board, n, m, i, j));
        }
    }
    return maxValue;
}