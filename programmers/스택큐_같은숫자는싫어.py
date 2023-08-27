def solution(arr):
    unique_list = []
    for num in arr:
        if unique_list == []: 
            unique_list.append(num)
        elif unique_list[-1] != num:
            unique_list.append(num)
            
    return unique_list