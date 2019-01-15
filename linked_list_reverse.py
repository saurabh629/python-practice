#!/usr/bin/python
'''
python program to print a linked list in reverse order
'''

class Node():
    def __init__(self,val,nxt):
    	self.nxt=nxt
   	self.val=val

def prnt(n):
    nxt=n.nxt
    print n.val,'->' 
    if nxt is not None:
    	prnt(nxt)
    
def reverse_linked_list(node,tail=None):
    nxt=node.nxt
    node.nxt=tail
    if nxt is None:
        return nxt
    else:
    	reverse_linked_list(nxt,node) 
    
def main():
    n0=Node(3,None)
    n1=Node(2,n0)
    n2=Node(1,n1)
    prnt(n2)    
    reverse_linked_list(n2)
    prnt(n0)

if __name__=='__main__':
    main()

