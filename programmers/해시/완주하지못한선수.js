function solution(participant, completion) {
    const participantMap = new Map()
    participant.forEach((p) => {
        participantMap.set(p, (participantMap.get(p) ?? 0) + 1)
    })
    for (let i = 0; i < completion.length; i++) {
        const value = participantMap.get(completion[i])
        if (value > 0) {
             participantMap.set(completion[i], value - 1)
        }
    }
    for (const [key, value] of participantMap.entries()) {
        if (value === 1) return key
    }
}