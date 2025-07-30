function solution(bridge_length, weight, truck_weights) {
    // 모두 다리 건널 때 최소 몇 초가 걸리는지
    // 큐 시뮬레이션
    const q = Array(bridge_length).fill(0); // 다리 길이(최대 길이 == bridge_length), 남은시간 저장
    let t = 0;
    let w = 0; // 다리에 올라간 총 무게
    while (q.length > 0) {
        t++;
        w -= q.shift();
        if (truck_weights.length > 0) {
            if (w + truck_weights[0] <= weight) {
                const truck = truck_weights.shift();
                w += truck;
                q.push(truck);    
            } else {
                q.push(0);
            }
        }
    };
    
    return t;
}