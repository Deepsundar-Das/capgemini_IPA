def remove_duplicate(list:list) -> set:
    s = {i for i in list if i > 5}
    return s 

print(remove_duplicate([1,2,2,3,5,6,8,89]))
