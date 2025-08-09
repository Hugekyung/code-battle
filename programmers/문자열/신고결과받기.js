function solution(id_list, report, k) {
    // 중복 제거
    const unique = [...new Set(report)];
    
    // 신고 횟수 집계
    const cnt = {};
    unique.forEach((r) => {
        const [user, target] = r.split(' ');
        cnt[target] = (cnt[target] || 0) + 1;
    });
    
    // 신고 처리자 집계
    const banned = new Set(Object.keys(cnt).filter((user) => cnt[user] >= k));
    
    // 신고자 집계용 객체 생성
    const result = {};
    id_list.forEach((id) => result[id] = 0);
    
    unique.forEach((r) => {
        const [user, target] = r.split(' ');
        if (banned.has(target)) {
            result[user]++
        }
    })

    return Object.values(result).map((cnt) => cnt);
}