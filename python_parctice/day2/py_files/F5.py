import logging
logging.basicConfig(
    filename="F5.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def reverse_string(s:str) -> str:
    logging.info(f"input : {s}")
    """
        reverse a input string 
        input :
            s(str) : input string
        output :
            str : returns the reverse of the original input string
    """
    rev = ""
    for i in s:
        rev = i + rev
    return rev

output = reverse_string(input("enter a String: "))
logging.info(f"output : {output}")
