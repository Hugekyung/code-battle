function solution(s) {
    const caseArr = [];
    const maxChunkSize = s.length / 2;
    for (let chunk = 1; chunk <= maxChunkSize; chunk++) {
        let result = '';
        let prev = s.substring(0, chunk);
        let cnt = 1;
        for (let i = chunk; i < s.length; i += chunk) {
            const curr = s.substring(i, i + chunk);
            if (prev === curr) {
                cnt++
                continue;
            }

            if (cnt === 1) {                
                result += prev;
            } else {
                result += cnt;
                result += prev;    
            }
            cnt = 1;
            prev = curr;
        }
        if (cnt === 1) {                
            result += prev;
        } else {
            result += cnt;
            result += prev;    
        }
        caseArr.push(result);
    }
    
    let minLength = s.length;
    caseArr.forEach((c) => {
        minLength = Math.min(minLength, c.length);
    })
    
    return minLength;
}