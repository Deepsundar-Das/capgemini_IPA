# not done
def create_set(list: list) -> set:
    div_set = {i for i in list if (i % 3 == 0 and i % 5 == 0 and i >=1 and i <= 50)}
    return div_set

print(create_set([1,6,45,35,15]))
