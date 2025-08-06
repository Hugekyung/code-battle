/* repository가 undefined인 경우 */
const object1 = {
  repository: undefined,
};

/* repository의 readme가 undefined인 경우 */
const object2 = {
  repository: {
    readme: undefined,
  },
};

/** repository.readme 모두가 존재하는 경우 */
const object3 = {
  repository: {
    readme: {
      extension: 'md',
      content: '금융을 쉽고 간편하게',
    }
  }
};

function safelyGet(obj, str) {
  const strArr = str.split('.');
  for (const str of strArr) {
    if (obj === undefined) {
      return undefined;
    }
    obj = obj[str]
  }

  return obj
}

console.log(safelyGet(object1, 'repository.readme.extension'))
console.log(safelyGet(object2, 'repository'))
console.log(safelyGet(object3, 'repository.readme'))