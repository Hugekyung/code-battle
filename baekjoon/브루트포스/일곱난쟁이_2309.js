// * 9명 중 2명을 찾는 경우의 수
// * 각 경우가 부합되는 경우인지 검증
// * 키 오름차순 정렬
function solution(originArr) {
    const sum = originArr.reduce((s, x) => s + x);
    const arr = originArr.sort((a, b) => a - b);
    for (let i = 0; i < arr.length; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            if (sum - arr[i] - arr[j] === 100) {
                for (const x of arr) {
                    if (x === arr[i] || x === arr[j]) {
                        continue;
                    }
                    console.log(x);
                }
                return;
            }
        }
    }
    return;
}

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");
const arr = input.map(Number);
solution(arr);
