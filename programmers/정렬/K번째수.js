function solution(array, commands) {
    return commands.map(([ i, j, k ]) => {
        const newArr = [...array].slice(i-1, j);
        newArr.sort((a, b) => a - b);
        return newArr[k-1];
    })
}