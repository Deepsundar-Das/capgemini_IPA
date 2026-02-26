import logging
logging.basicConfig(
    filename="F7.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def find_missing_number(list : list) -> int:
    logging.info(f"input : {list}")
    """
        finds missing number in a list, the missing number should be in between 1 to N, N cannot be a missing number
        [1,2,4,5,6] -> valid, here you can say 3 is missing
        [1,2,3,4,5] -> invalid, you cannot say 6 is missing 
        input : 
            list(list) : input a list 
        output : 
            int : returns the number which is missing in the given list
    """
    sum = 0
    max = -1
    total_sum = 0
    for i in list:
        if i > max :
            max = i
        sum += i
    n = len(list)
    total_sum = ((max+1)*max)//2
    return (total_sum - sum)

output = find_missing_number(eval(input("enter a list: ")))
logging.info(f"output : {output}")
