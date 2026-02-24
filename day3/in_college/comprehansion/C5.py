def cub_num(list: list) -> dict:
    dictionary = {i: i ** 3 for i in list if i >= 1 and i <=5}
    return dictionary

print(cub_num([1,2,4,6,7]))
