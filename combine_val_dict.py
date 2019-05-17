#!/usr/bin/python
'''
Python program to combine values of the same keys in python list of dictionaries.
e.g. 
    [{'item': 'item1', 'amount': 400}, 
          {'item': 'item2', 'amount': 300}, 
          {'item': 'item1', 'amount': 750},
          {'item': 'item2', 'amount': 900}]
          
    result=[{'item2': 1200, 'item1': 1150}]
'''

from collections import Counter

def combine_values_dict(Data):
    result = Counter()
    for d in Data:
        result[d['item']]=result[d['item']]+d['amount']
    return result

def main():
    Data=[{'item': 'item1', 'amount': 400}, 
          {'item': 'item2', 'amount': 300}, 
          {'item': 'item1', 'amount': 750},
          {'item': 'item2', 'amount': 900}]
    print combine_values_dict(Data)

if __name__=='__main__':
    main()
