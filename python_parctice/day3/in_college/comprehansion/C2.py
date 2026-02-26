def extract_vowels(s:str) -> list:
    lst = [word for word in s.split() if word[0].lower() in 'aeiou']
    return lst

print(extract_vowels('I am deep'))
