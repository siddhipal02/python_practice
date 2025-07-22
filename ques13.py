def avg(list):
    sum=0
    for i in list:
        sum= sum+ i
    avg= sum/len(list)
    print(avg)
list=[1,2,3,4,5]
avg(list)