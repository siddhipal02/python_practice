
import math
def isPrime(n):
    if(n==0 or n==1):
        print("not a prime number")
    else:
            for i in range(2, int(math.sqrt(n))+1):
                if (n%i == 0):
                    print("not a prime number")
                    return
            print("prime number")

isPrime(13)

