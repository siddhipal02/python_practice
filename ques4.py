def isLeap(year):
    if(year%4==0):
        if((year%100 != 0) or (year%400 ==0)):
            print("leap year")
            return
    print("not a leap year")

isLeap(2025)