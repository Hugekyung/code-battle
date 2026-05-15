// 2번 문제 - different_products
// 원소 하나를 제거했을 떄 나머지 원소들의 곱의 경우의 수
function solution(A) {
    const setArr = new Set(A); // 중복 원소가 있어봐야 곱셈 결과가 모두 중복임. 따라서 중복 원소를 제거하고 원소의 개수를 반환하면 됨.
    return setArr.size;
}