#!/bin/python
'''
substrCount() will return a count of palindrome substring of the original string s

'''

# Complete the substrCount function below.
def substrCount(s):
    ListOfSubstrings=[]
    count=0
    n=len(s)
    PalindromeList=[]
    for i in xrange(n):
        for j in xrange(i,n):
            ListOfSubstrings.append(s[i:j+1])
    for item in ListOfSubstrings:
        s1=item
        list1=list(item)
        list1.reverse()
        s2=''.join(list1)
        if s1==s2:
            count=count+1
	    PalindromeList.append(s1)
    return (PalindromeList, count)

if __name__ == '__main__':

    s = raw_input("Enter the string to be check:\n")

    result = substrCount(s)
    print "List of Palindrome substrings:\n", result[0]
    print "Count of Palindrome substrings:\n", result[1]


