function solution(today, terms, privacies) {
    // terms Map 객체 생성
    const termsMap = new Map();
    terms.forEach((t) => {
        const [a, b] = t.split(' ');
        termsMap.set(a, b);
    })
    
    // privacies 순회하면서 today, terms 기준 파기해야할 정보인지 확인
    const result = privacies.map((p, i) => {
        const [date, term] = p.split(' ');
        const limitMonth = termsMap.get(term);
        if (checkDate(today, date, limitMonth)) {
            // 유효기간이 지난 경우 true
            return i + 1;
        }
    }).filter(Boolean);
    return result;
}

function checkDate(today, date, limitMonth) {
    const [tyear, tmonth, tday] = today.split('.');
    const [year, month, day] = date.split('.');
    
    // 월 단위 치환
    const calYear = (tyear - year) > 0 ? (tyear - year) * 12 : 0;
    const calMonth = tmonth - month;
    const calday = tday - day;
    
    // 오늘 날짜와 약관 시작일 날짜 사이 기간을 월 단위로 계산
    const calculMonth = calYear + calMonth;
    if (limitMonth < calculMonth) {
        return true; // 유효기간 지남
    } else if (limitMonth == calculMonth && calday >= 0) {
        return true; // 유효기간 지남
    }
}