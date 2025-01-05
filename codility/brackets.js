function solution(S) {
    const stack = [];
    for (const str of S) {
        if (str == "{" || str == "[" || str == "(") stack.push(str);
        else {
            if (str == "}") {
                if (stack[stack.length - 1] != "{") return 0;
            } else if (str == ")") {
                if (stack[stack.length - 1] != "(") return 0;
            } else {
                if (stack[stack.length - 1] != "[") return 0;
            }
            stack.pop();
        }
    }

    return stack.length === 0 ? 1 : 0;
}
