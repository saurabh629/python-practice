#!/bin/python


# read the last n lines from a file opened
def read_lastn(str, n):
    k = str.split('\n')
    k.reverse()
    for i in range(0,len(k)):
        if i<n:
            print k[i]

if __name__ == '__main__':
    f=open('emails.log','r')
    n=2
    print read_lastn(f.read(),n)
