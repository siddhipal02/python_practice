list=[2,5,4,9,1,8]
def selectionSort(list):
    n= len(list)
    for i in range(n-1):
        smallestIdx=i
        for j in range(i+1, n):
            if(list[j]< list[smallestIdx]):
                smallestIdx=j
        list[i], list[smallestIdx] = list[smallestIdx], list[i]


def printList(list):
    for i in list:
        print (i, end=" ")
selectionSort(list)
printList(list)
