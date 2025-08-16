function solution(s) {
    const arr = [];
    const ss = s.slice(1, s.length-1).split('},');
    for (let i = 0; i < ss.length; i++) {
        const numStr = ss[i].replaceAll('{', '').replaceAll('}', '');
        const numArr = numStr.split(',');
        arr.push(numArr);
    }
    const sorted = arr.sort((a, b) => a.length - b.length);
    
    // 방법 1: 모든 원소를 한 곳에 모은 뒤 Set 함수로 중복 원소 제거
    const temp = [];
    sorted.forEach((arr) => {
        arr.forEach((n) => temp.push(Number(n)));
    })
    const result = [...new Set(temp)];
    
    // 방법 2: 각 배열의 원소를 순회하며 result 배열에 없는 값만 순차적으로 push
    // const result = [];
    // sorted.forEach((nArr) => {
    //     if (nArr.length === 1) {
    //         result.push(Number(nArr[0]));
    //     } else {
    //         nArr.forEach((n) => {
    //             if (!result.includes(Number(n))) {
    //                 result.push(Number(n));
    //             }
    //         })
    //     }
    // })
    return result;
}