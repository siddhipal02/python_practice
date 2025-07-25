import math
import datetime
def isPrime(n):
    if(n==0 or n==1):
        print("not a prime number")
    else:
            for i in range(2, int(math.sqrt(n))+1):
                if (n%i == 0):
                    print("not a prime number")
                    return
            print("prime number")



def divisibleBy(n):
    if(n%3==0 or n%5==0):
        print("dividible")
    else:
        print("not divisible")    



def sum():
     sum= 0
     for i in range(1, 101):
          if(i%2 == 0):
              sum= sum+i



def isLeap(year):
    if(year%4==0):
        if((year%100 != 0) or (year%400 ==0)):
            print("leap year")
            return
    print("not a leap year")


def factorial(n):
    fact=1
    for i in range (n,0,-1):
        fact = fact*i
    print(fact)



def countWords(str):
    count =0
    for i in range(len(str)):
        count= count+1
    print(count)



def largest(a,b,c):
    if(a>b and a>c):
        print("a is the largest")
    elif(b>a and b>c):
        print("b is the largest")
    else:
        print("c is the largest")

def week(ch):
    match ch:
       case 1:
        print("MONDAY")
       case 2:
        print("TUESDAY")
       case 3:
        print("WEDNESDAY")
       case 4:
        print("THURSDAY")
       case 5:
        print("FRIDAY")
       case 6:
        print("SATURDAY")
       case 7:
        print("SUNDAY")



def reverse(n):
    rev=0
    while(n>0):
        digit= n%10
        rev= rev*10 + digit
        n=n//10
    print(rev)



def check(ch):
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    elif ch.isalpha():
        print("Consonant")
    else:
        print("Not an alphabet")



def table(n):
    for i in range(1,11):
        print(n,"*" ,i ,"=",n*i)


def check(n):
    if(n>0):
        print("positive")
    elif(n<0):
        print("negative")
    else:
        print("zero")


def avg(list):
    sum=0
    for i in list:
        sum= sum+ i
    avg= sum/len(list)
    print(avg)



def fibo(n):
      a, b = 0, 1
      print("Fibonacci series:")
      for i in range(n):
         print(a, end=" ")
         a, b = b, a + b



def check(ch):
    if ch.isalpha():
       print("Alphabet")
    elif ch.isdigit():
       print("Digit")
    else:
       print("Special character")



def season(month):
    if month in [12, 1, 2]:
        print("Winter")
    elif month in [3, 4, 5]:
        print("Spring")
    elif month in [6, 7, 8]:
        print("Summer")
    elif month in [9, 10, 11]:
        print("Autumn")
    else:
        print("Invalid month number")


def countVowels(text, vowels):
    count = 0
    for ch in text:
       if ch in vowels:
         count += 1

    print("Number of vowels:", count)




def calc(a,b,op):
    match op:
       case '+':
          print(a + b)
       case '-':
          print(a - b)
       case '*':
          print(a * b)
       case '/':
          if b != 0:
            print(a / b)
          else:
            print("Cannot divide by zero")
       case default:
          print("Invalid operator")



def greater(list,limit):
    print("Elements greater than", limit, ":")
    for num in list:
       if num > limit:
          print(num)

    
def checkPalindrome(word):
    rev = word[::-1]
    if rev == word:
        print("Palindrome")
    else:
        print("Not Palindrome")



n = int(input("Enter a number: "))
match n:
    case 1:
        x= datetime.datetime.now()
        isPrime(13)
        y= datetime.datetime.now()
        z= y-x
        print("time taken by this function:", z)
    case 2:
        x= datetime.datetime.now()
        divisibleBy(2) 
        y= datetime.datetime.now() 
        z= y-x
        print("time taken by this function:", z)
    case 3:
        x= datetime.datetime.now()
        sum()
        y= datetime.datetime.now() 
        z= y-x
        print("time taken by this function:", z)
    case 4:
        x= datetime.datetime.now()
        isLeap(2025)
        y= datetime.datetime.now()
        z= y-x
        print("time taken by this function:", z)
    case 5:
        x= datetime.datetime.now()
        factorial(4)
        y= datetime.datetime.now()
        z= y-x
        print("time taken by this function:", z)
    case 6:
        x= datetime.datetime.now()
        countWords("abcdef")
        y= datetime.datetime.now()
        z= y-x
        print("time taken by this function:", z)
    case 7:
        x= datetime.datetime.now()
        largest(2,3,4)
        y= datetime.datetime.now()
        z= y-x
        print("time taken by this function:", z)
    case 8:
        x= datetime.datetime.now()
        week(3)
        y= datetime.datetime.now()
        z= y-x
        print("time taken by this function:", z)
    case 9:
        x= datetime.datetime.now()
        reverse(123)
        y= datetime.datetime.now()
        z= y-x
        print("time taken by this function:", z)
    case 10:
        x= datetime.datetime.now()
        check('e')
        y= datetime.datetime.now()
        z= y-x
        print("time taken by this function:", z)
    case 11:
        x= datetime.datetime.now()
        table(4)
        y= datetime.datetime.now()
        z= y-x
        print("time taken by this function:", z)
    case 12:
        x= datetime.datetime.now()
        check(9)
        y= datetime.datetime.now()
        z= y-x
        print("time taken by this function:", z)
    case 13:
        x= datetime.datetime.now()
        list=[1,2,3,4,5]
        avg(list)
        y= datetime.datetime.now()
        z= y-x
        print("time taken by this function:", z)
    case 14:
        x= datetime.datetime.now()
        fibo(5)
        y= datetime.datetime.now()
        z= y-x
        print("time taken by this function:", z)
    case 15:
        x= datetime.datetime.now()
        ch = input("Enter a character: ")
        check(ch)
        y= datetime.datetime.now()
        z= y-x
        print("time taken by this function:", z)
    case 16:
        x= datetime.datetime.now()
        season(5)
        y= datetime.datetime.now()
        z= y-x
        print("time taken by this function:", z)
    case 17:
        x= datetime.datetime.now()
        text = "Hello World"
        vowels = "aeiouAEIOU"
        countVowels(text,vowels)
        y= datetime.datetime.now()
        z= y-x
        print("time taken by this function:", z)
    case 18:
        x= datetime.datetime.now()
        calc(10,5,'+')
        y= datetime.datetime.now()
        z= y-x
        print("time taken by this function:", z)
    case 19:
        x= datetime.datetime.now()
        list = [10, 25, 3, 40, 5]
        limit = 10
        greater(list,limit)
        y= datetime.datetime.now()
        z= y-x
        print("time taken by this function:", z)
    case 20:
        x= datetime.datetime.now()
        text = "nun"
        checkPalindrome(text)
        y= datetime.datetime.now()
        z= y-x
        print("time taken by this function:", z)
