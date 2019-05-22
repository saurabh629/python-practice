#!/usr/bin/python
'''
Python program to convert input time in 24 hour format. Write result to file.
e.g. INPUT: 07:05:45PM
     OUTPUT: 19:05:45
'''
import os
import sys

def timeConversion(s):
    lista=s.rstrip('APM').split(':')
    print (lista)
    hour=int(lista[0])
    second=lista[2]
    if 'PM' in s and hour < 12:
        hour+=12
    lista[0]=str(hour)
    result=":".join(lista)
    return result

if __name__=='__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    print (result)
    f.write(result + '\n')
    f.close()

