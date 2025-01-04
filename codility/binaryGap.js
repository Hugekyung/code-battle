function solution(N) {
    // 2진수로 변환(2로 나눈 나머지 배열 저장 -> 몫이 1이 될 때까지 반복)
    // 가장 큰 binarygap 구하기
    let binary = "";
    while (N > 0) {
        const rest = N % 2;
        binary = rest + binary;
        N = Math.floor(N / 2);
    }

    let maxBinaryGap = 0;
    let nowBinaryGap = 0;
    for (const b of binary) {
        if (b === "0") nowBinaryGap += 1;
        else {
            maxBinaryGap = Math.max(maxBinaryGap, nowBinaryGap);
            nowBinaryGap = 0;
        }
    }
    return maxBinaryGap;
}
