function solution(record) {
    let userObj = {};
    record.forEach((r) => {
        const [doing, userId, nickname] = r.split(' ');
        if (doing === 'Enter' || doing === 'Change') {
            userObj[userId] = nickname;    
        }
    });
    const result = record.map((r) => {
        const [doing, userId, nickname] = r.split(' ');
        const msg = doing === 'Enter' ? `${userObj[userId]}님이 들어왔습니다.` : doing === 'Leave' ? `${userObj[userId]}님이 나갔습니다.` : null;
        return msg;
    }).filter(Boolean);
        
    return result;
}