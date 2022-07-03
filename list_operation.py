 # l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" ,
 # 234:[23,45,656]}]
import logging
logging.basicConfig(filename="listoperation.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')
class list_operation:
    def reverse(self,list1):
        list_rev = list1[::-1]
        logging.info("The reveresd list is: ")
        logging.info(list_rev)
    def list_extration(self,list1):
        logging.info("List available inside list elemnts are: ")

        for i in list1:
            if type(i) == list:
                print(i)
                logging.info(i)

list_object  = list_operation()
try:
    list1 = (1,2,3,4)
    if len(list1) == 0:
        raise ValueError("Empty String")
    if type(list1) != list:
        raise TypeError("Entered input type is not list")
    list_object.reverse(list1)
    list_object.list_extration(list1)
except (ValueError, TypeError) as e:
    logging.exception(e)
    logging.info("No task is performed")

