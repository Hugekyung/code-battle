function solution(fees, records) {
    const [baseTime, baseFee, unitMin, unitFee] = fees;
    const spendTimeMap = new Map();
    // IN 기록만 Map 객체등록
    const inMap = new Map();
    for (const record of records) {
        const [time, carNum, inout] = record.split(' ');
        if (inMap.get(carNum)) {
            // 입차 내역이 있을 경우 사용 시간 계산
            let spendTime = calculateSpendTime(inMap.get(carNum), time);
            if (spendTimeMap.has(carNum)) {
                spendTime += spendTimeMap.get(carNum);
                spendTimeMap.set(carNum, spendTime);
            } else {
                spendTimeMap.set(carNum, spendTime);
            }
            
            // 요금 계산 후 Map에서 제거
            inMap.delete(carNum);
        } else {
            // 입차 내역이 없으면 Map 객체 등록
            inMap.set(carNum, time);
        }
    }
    
    // Map에 남은 IN이 있으면 23:59분에 출차한 것으로 처리
    inMap.forEach((inTime, carNum, map) => {
        const outTime = '23:59';
        let spendTime = calculateSpendTime(inTime, outTime);
        if (spendTimeMap.has(carNum)) {
            spendTime += spendTimeMap.get(carNum);
            spendTimeMap.set(carNum, spendTime);
        } else {
            spendTimeMap.set(carNum, spendTime);
        }
    })
    
    const spendTimes = Array.from(spendTimeMap.values()).map((st) => calculateFee(st));
    const carNumbers = Array.from(spendTimeMap.keys());
    
    // 차량 번호 작은 것부터 큰순으로 정렬
    return spendTimes.map((fee, idx) => ({ fee, num: Number(carNumbers[idx]) }))
                .sort((a, b) => a.num - b.num)
                .map(obj => obj.fee);
    
    function calculateSpendTime(inTime, outTime) {
        const [inHour, inMin] = inTime.split(':');
        const [outHour, outMin] = outTime.split(':');
        const spendMinute = Number(+outHour - +inHour) * 60 + Number(+outMin - +inMin);
        return spendMinute;
    }
    
    function calculateFee(spendMinute) {
        if (baseTime < spendMinute) {
            return baseFee + (Math.ceil((spendMinute - baseTime) / unitMin)) * unitFee;
        }
        return baseFee;
    }
}