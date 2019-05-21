#!/usr/bin/python
'''
Find the average marks of specific student from student_marks dictionary
eg. { Amir : [ 2, 4, 3], Bob : [ 1, 3, 1] }
    query name - Amir
    result = 3

'''
def find_average(student_marks,name):
    result=count=0
    for key,value in student_marks.items():
        if key==name:
            for i,item in enumerate(value):
                result+=item
                count+=1
            result=result/count
    return result

if __name__=='__main__':
    n=int(input("Enter the number of students:"))
    student_marks={}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name]=scores
    name=input("Enter the name of student:")
    print ('Average marks of {0} is {1:.2f}'.format(name,find_average(student_marks,name)))
