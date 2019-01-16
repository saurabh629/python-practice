'''
Write a Python program to read last n lines of a file

'''

# !/usr/bin/python

def file_read(fname):
    txt = open(fname)
    print(txt.read())

def file_read_lines(fname,n):
    with open(fname) as f:
        #Content_list is the list that contains the read lines.     
        content_list = f.readlines()
    l = len(content_list)
    for item in range(l-n,l) :
        print content_list[item]

def main():
    # read all the lines of the files
    file_read('test.txt')
    # read last n lines of the files
    file_read_lines('test.txt', 3)

if __name__ == '__main__':
   main()
 
