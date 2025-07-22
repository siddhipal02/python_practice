list=[2,5,4,9,1,8]
target=8
def linearSearch(list, target):
    for i in list:
        if(i== target):
            return i
    return -1
item= linearSearch(list,target)
print(item)
