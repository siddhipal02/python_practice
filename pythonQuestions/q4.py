def removeDuplicates(list):
    new_list=[]
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

list=[1,2,3,4,5,1,2,3,4,5]
print(removeDuplicates(list))
