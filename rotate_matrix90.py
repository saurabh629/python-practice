
#rotate matrix by 90 degree anticlockwise.

def rotate90_antic(arr):
    result = []
    i=0
    j=0
    for i in range(0,len(arr)):
        arr[i].reverse()
    for j in range(0,len(arr)):
        rows=[]
        for i in range(0,len(arr)):
            rows.append(arr[i][j])
        result.append(rows)
    return result
    
if __name__ == '__main__':
 
    arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    x=rotate90_antic(arr)
    print x
    
    arr=[[1,2,3],[4,5,6],[7,8,9]]
    x=rotate90_antic(arr)
    print x
