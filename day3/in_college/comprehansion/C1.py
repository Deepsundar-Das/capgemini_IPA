def square_list(list:list) -> list:
    new_list = [i ** 2 for i in list if i % 2 == 0 ]
    return new_list

print(square_list([1,2,3,4,5]))
