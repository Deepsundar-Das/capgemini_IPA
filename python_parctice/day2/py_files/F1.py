import logging
logging.basicConfig(
    filename="F1.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def count_vowels(s:str) -> int:
    logging.info(f"input : {s}")
    """ 
        returns total number of vowels present in a string
        params :
            s(str) : input string
        output:
            int : returns total count of vowels present in s string
    """
    count = 0
    for i in s:
        if i in 'aeiou':
            count += 1
    return count


number_of_vowels = count_vowels(input("enter a string to count vowels: "))
logging.info(f"output : {number_of_vowels}")

