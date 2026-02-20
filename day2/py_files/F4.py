import logging
logging.basicConfig(
    filename="F4.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def checkAsc(list : list) -> bool:
    logging.info(f"input is : {list}")
    for i in range (1, len(list) - 1):
        if (list[i] < list[i-1]):
            return False
    return True

c = checkAsc([1,2,3,4,5])
logging.info(f"output is : {c}")

