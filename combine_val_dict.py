#!/usr/bin/python
'''
Python program to combine values in python list of dictionaries.
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
