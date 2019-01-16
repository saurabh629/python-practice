#!/usr/bin/python3

'''
 sorting python dictionary by their key
'''

def sort_dict_by_key_ascending(dict):
    print ("Sorting the dict by key in ascending order")
    for key in sorted(dict.keys()):
        print ("{0}: {1}".format(key, dict[key]))
def sort_dict_by_key_descending(dict):
    print ("Sorting the dict by key in descending order")
    for key in sorted(dict.keys(), reverse=True):
        print ("{0}: {1}".format(key, dict[key]))

def main():
   my_dict = {'coins':7, 'pens':6, 'cups':5, 'bags':1, 'bottles':4, 'books':5}
   sort_dict_by_key_ascending(my_dict)
   sort_dict_by_key_descending(my_dict)

if __name__=='__main__':
    main()
    
