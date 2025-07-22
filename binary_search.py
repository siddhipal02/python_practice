list=[2,5,4,9,1,8]
target=1
def binarySearch(list, target):
    low=0
    high= len(list)-1
    list.sort()
    #list=sorted(list)
    while(low<=high):
        mid= (low+high)//2
        if(target<list[mid]):
            high=mid-1
        elif(list[mid] == target):
            print("found")
            return  
        else:
            low= mid+1
    print("not found")
            
binarySearch(list, target)
