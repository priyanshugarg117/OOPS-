# l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" ,
 # 234:[23,45,656]}]
import logging
logging.basicConfig(filename="dictoperation.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')
class dict_operation:
    def all_dic(self,list1):
        flag = 0
        for i in list1:

            if type(i) == dict:
                flag = flag + 1
                #print(flag)
                logging.info("All Dictionary elements in given list are: ")
                #print(i)
                logging.info(i)
        if flag == 0:
            logging.info("No Dictionary found in given list")
    def all_key(self,list1):
        flag = 0
        for i in list1:
            if type(i) == dict:
                flag = flag + 1
                logging.info("All Dictionary keys are: ")
                logging.info(i.keys())
        if flag == 0:
            logging.info("No dictionary found in given list")
    def all_values(self,list1):
        flag = 0
        for i in list1:
            if type(i) == dict:
                flag = flag + 1
                logging.info("All Dictionary values are: ")
                logging.info(i.values())
        if flag == 0:
            logging.info("No dictionary found in given list")

list_object  = dict_operation()
try:
    list1 = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6),{"key1" :"sudh" ,
 234:[23,45,656]} ]
    if len(list1) == 0:
        raise ValueError("Empty list")
    if type(list1) != list:
        raise TypeError("Entered input type is not list")
    list_object.all_dic(list1)
    list_object.all_key(list1)
    list_object.all_values(list1)

except (ValueError, TypeError) as e:
    logging.exception(e)
    logging.info("No task is performed")

