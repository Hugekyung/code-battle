function solution(str1, str2) {
    const re = /^[A-Z]{2}/
    str1 = str1.toUpperCase();
    str2 = str2.toUpperCase();
    
    // str1
    const str1Arr = [];
    for (let i = 0; i < str1.length; i++) {
        const s = str1.substring(i, i+2);
        if (re.test(s)) {
            str1Arr.push(s);
        }
    }

    // str2
    const str2Arr = [];
    for (let i = 0; i < str2.length - 1; i++) {
        const s = str2.substring(i, i+2);
        if (re.test(s)) {
            str2Arr.push(s);
        }
    }
    
    if (str1Arr.length === 0 && str2Arr.length === 0) return 65536;
    
    const unique = new Set([...str1Arr, ...str2Arr]);
    let intersection = [];
    let union = [];
    for (const u of unique) {
        let cnt1 = findMatchedString(str1Arr, u).length;
        let cnt2 = findMatchedString(str2Arr, u).length;
        
        // 교집합
        const intersecCnt = Math.min(cnt1, cnt2);
        const arr1 = new Array(intersecCnt).fill(u)
        intersection = [...intersection, ...arr1];
        
        // 합집합
        const unionCnt = Math.max(cnt1, cnt2);
        const arr2 = new Array(unionCnt).fill(u)
        union = [...union, ...arr2];
    }
    const jacade = intersection.length / union.length;
    return Math.floor(jacade * 65536);
}

function findMatchedString(arr, s) {
    return arr.filter((value) => value === s);
}