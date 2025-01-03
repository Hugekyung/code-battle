// const input = `
// 4 6
// 0 0 0 0 0 0
// 1 0 0 0 0 2
// 1 1 1 0 0 2
// 0 0 0 0 0 2
// `.trim();
// const lines = input.split("\n");

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");
const arr = input.map((l) => l.split(" ").map(Number));
const n = arr[0][0];
const m = arr[0][1];
const lab = arr.slice(1);
let max_cnt = 0;

function bfs() {
    const lab_copy = JSON.parse(JSON.stringify(lab)); // * 깊은 복사
    const dq = [];
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (lab[i][j] === 2) {
                dq.push({ x: i, y: j });
            }
        }
    }

    const dx = [1, -1, 0, 0];
    const dy = [0, 0, -1, 1];
    while (dq.length > 0) {
        const { x, y } = dq.shift();
        for (let i = 0; i < 4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
                continue;
            }
            if (lab_copy[nx][ny] === 0) {
                lab_copy[nx][ny] = 2;
                dq.push({ x: nx, y: ny });
            }
        }
    }

    let now_cnt = 0;
    lab_copy.forEach((row) => {
        row.forEach((cell) => {
            if (cell === 0) {
                now_cnt += 1;
            }
        });
    });
    max_cnt = Math.max(max_cnt, now_cnt);
    return;
}

function makeWall(cnt) {
    if (cnt === 3) {
        bfs();
        return;
    }

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (lab[i][j] === 0) {
                lab[i][j] = 1;
                makeWall(cnt + 1);
                lab[i][j] = 0;
            }
        }
    }
    return;
}

// * 벽 세우기
makeWall(0);
console.log(max_cnt);
