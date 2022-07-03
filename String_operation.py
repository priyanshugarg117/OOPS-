import logging
logging.basicConfig(filename="stringoperation.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')
class string_operation:
    def extract(self, str):
        ext = str[::3]
        logging.info("extracted data from index one to last with a jump of 3 is: ")
        logging.info(ext)
    def reverse_user(self,str):
        rev = str[::-1]
        logging.info("reversed entered string without using reverse function will be: ")
        logging.info(rev)
    def split_upper(self,str):
        str1 = str.upper()
        logging.info("Upper and splitted string will be: ")
        logging.info(str1.split())
    def lower_string(self,str):
        lower = str.lower()
        logging.info("whole string into lower case is: ")
        logging.info(lower)


str_input = input("Please enter your string: ")
try:
    if len(str_input) == 0:
        raise ValueError("Empty string")
    op = string_operation()
    op.extract(str_input)
    op.reverse_user(str_input)
    op.split_upper(str_input)
    op.lower_string(str_input)
except ValueError as e:
    logging.exception(e)
    logging.info("No task performed since string length is zero")
print(op.lower_string(str_input))





