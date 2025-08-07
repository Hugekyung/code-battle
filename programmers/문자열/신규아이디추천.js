function solution(new_id) {
    // 1단계
    new_id = new_id.toLowerCase();
    // 2단계
    new_id = new_id.replace(/[^a-z0-9._-]/g, '');
    // 3단계
    new_id = new_id.replace(/\.{2,}/g, '.');
    // 4단계
    if (new_id.startsWith('.')) {
        new_id = new_id.substring(1);
    }
    if (new_id.endsWith('.')) {
        new_id = new_id.substring(0, new_id.length-1);
    }
    // 5단계
    if (new_id === '') {
        new_id = 'a';
    }
    // 6단계
    if (new_id.length >= 16) {
        new_id = new_id.slice(0, 15);
        if (new_id[new_id.length-1] === '.') {
            new_id = new_id.slice(0, new_id.length-1);
        }
    }
    // 7단계
    if (new_id.length <= 2) {
        const iter = 3 - new_id.length;
        for (let i = 0; i < iter; i++) {
            new_id = new_id + new_id[new_id.length-1];    
        }
    }
    return new_id;
}