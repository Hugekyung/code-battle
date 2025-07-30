function solution(arr)
{
    const stack = [];
    for (const num of arr) {
        if (stack[stack.length - 1] === num) {
            continue
        }
        stack.push(num)
    }
    return stack
}