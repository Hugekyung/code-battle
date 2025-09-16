function solution(A) {
    const positiveSet = new Set(A.filter((a) => a > 0));
    for (let i = 1; i <= positiveSet.size + 1; i++) {
        if (!positiveSet.has(i)) {
            return i;
        }
    }
}
