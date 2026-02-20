import logging
logging.basicConfig(
    filename="F2.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def count_character(s:str) -> int:
    logging.info(f"input String : {s}")
    """
        counts frequency of every characters in the input string
        input:
            s(str) : input string
        output:
            int : returns frequency of all the characters in the input string in a dictionary
    """

    char_count={}
    for i in s:
        if i not in char_count:
            char_count.update({i:1})
        else:
            current_freq=char_count.get(i)
            char_count.update({i:current_freq+1})
    return char_count


output = count_character(input("enter a string to count all the character frequency: "))
logging.info(f"output : {output}")
