function solution(X, A) {
    // 1 ~ X 사이의 모든 원소가 존재할 때의 K를 반환
    // X와 같거나 X보다 작은 나뭇잎 위치를 set 객체에 저장
    // 길이가 X가 되면 모든 원소가 있다는 것이므로, 그때의 K를 반환
    const visited = new Set();
    for (let i = 0; i < A.length; i++) {
        if (A[i] <= X) {
            visited.add(A[i]);
        }
        if (visited.size === X) {
            return i;
        }
    }
    return -1;
}
