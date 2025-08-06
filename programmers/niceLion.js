function solutions(str) {
    let idx = 0;
    const result = [];
    while (idx < str.length - 1) {
        if (str[idx] === str[idx+1] && str[idx] === str[idx+2]) {
            result.push(Number(str.substring(idx, idx+3)));
            idx = idx + 3;
            continue;
        }
        idx++
    }
    if (result.length === 0) return -1;
    return Math.max(...result);
}

console.log(solutions("12223"))
console.log(solutions("111999333"))
console.log(solutions("123"))