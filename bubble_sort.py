list=[2,5,4,9,1,8]
def bubbleSort(list):
    n= len(list)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if(list[j]>list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]
                
def printList(list):
    for i in list:
        print (i, end=" ")
bubbleSort(list)
printList(list)