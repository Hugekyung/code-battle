function solution(progresses, speeds) {
    const stack = []; // 완료된 작업 스택
    while (progresses.length > 0) {
        for (let i = 0; i < progresses.length; i ++) {
            progresses[i] += speeds[i]
        }
        
        let deployCnt = 0
        if (progresses[0] >= 100) {
            deployCnt += 1 // 첫번째 값이 배포 대상임
            for (let i = 1; i < progresses.length; i ++) {
                if (progresses[i] < 100) {
                    break;
                }
                deployCnt += 1
            }
        }
        
        if (deployCnt > 0) {
            stack.push(deployCnt);
            for (let i = 0; i < deployCnt; i ++) {
                progresses.shift();
                speeds.shift();
            }
        }
    }
    
    return stack
}