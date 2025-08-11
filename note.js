const arr = new Array(1, 2, 3);
const arr2 = Array(1, 2, 3);
const arr3 = Array(3).fill(4);
const arr4 = structuredClone(arr3);
arr4.push(4);

console.log(arr);
console.log(arr2);
console.log(arr3);
console.log(arr4);