list=[1,2,3,4,5,6,7,8,9,10]
def pairSum(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]+list[j]==10:
                print(list[i],list[j])

pairSum(list)