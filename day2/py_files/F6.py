import logging
logging.basicConfig(
    filename="F6.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def remove_duplicate(list:list) -> list:
    logging.info(f"input: {list}")
    """
        remove duplicate elements from a list while preserving the order
        input :
            list(list) : takes list as an input
        output : 
            returns a list with unique elements
    """

    dictionary = {}
    end =  len(list)
    i = 0
    while i < end:
        if list[i] not in dictionary:
            dictionary.update({list[i]:1})
            i += 1
        else:
            list.pop(i)
            end -= 1
    return list

output = remove_duplicate(eval(input("enter a list: ")))
logging.info(f"output : {output}")

