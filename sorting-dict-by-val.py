#!/usr/bin/python3

'''
 sorting python dictionary by their values 
'''

def sort_dict_by_value_ascending(dict):
    print ("Sorting the dict by values in ascending order")
    for key,value in sorted(dict.items(), key=lambda kv: kv[1]):
        print ("{0}: {1}".format(key, value))
def sort_dict_by_value_descending(dict):
    print ("Sorting the dict by values in descending order")
    for key,value in sorted(dict.items(), key=lambda kv: kv[1], reverse=True):
        print ("{0}: {1}".format(key, value))

def main():
   my_dict = {'coins':7, 'pens':6, 'cups':5, 'bags':1, 'bottles':4, 'books':5}
   sort_dict_by_value_ascending(my_dict)
   sort_dict_by_value_descending(my_dict)

if __name__=='__main__':
    main()
    
