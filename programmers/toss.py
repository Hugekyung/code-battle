input_string = input()
def get_greate_numbers(input_string):
    greate_numbers = []
    for i, s in enumerate(input_string):
        greate_num = s
        for j, st in enumerate(input_string[i+1:]):
            if s == st:
                greate_num += st
            if len(greate_num) == 3:
                greate_numbers.append(int(greate_num))
                break
    
    if len(greate_numbers) == 0:
        return -1
    greate_numbers.sort()
    return greate_numbers[-1]

print(get_greate_numbers(input_string))