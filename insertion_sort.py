list=[2,5,4,9,1,8]
def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while (j >= 0 and list[j] > key):
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key

def printList(list):
    for i in list:
        print (i, end=" ")
insertionSort(list)
printList(list)