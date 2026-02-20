import logging
logging.basicConfig(
    filename="F3.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def second_largest(lis : list) -> int:
    """
        finds the second largest element from the list
        params:
            list(list) : input list 
        output:
            int : returns second largest element from the integer list
    """
    largest = -1
    second_larg = -1
    for i in lis:
        if (i > largest):
            second_larg = largest
            largest = i
    return second_larg
    
a = second_largest([2,4,6,1,7,8])
logging.info(f"the output is {a}")

