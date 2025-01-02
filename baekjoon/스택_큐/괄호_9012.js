function solution(s) {
    const stack = [];
    for (const i of s) {
        if (i === "(") {
            stack.push(i);
        } else {
            if (stack.length > 0) {
                stack.pop();
            } else {
                return "NO";
            }
        }
    }
    return stack.length === 0 ? "YES" : "NO";
}

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");
const n = Number(input[0]);
for (let i = 1; i <= n; i++) {
    const s = input[i];
    console.log(solution(s));
}
