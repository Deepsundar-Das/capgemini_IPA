def student_score(dictionary : dict) -> dict:
    dict_keys = dictionary.keys()
    new_dictionary = {key : dictionary.get(key) for key in dict_keys if (dictionary.get(key) >= 60)}
    return new_dictionary

print(student_score({'s1':60, 's2':50, 's3':70}))
