def check(ch):
    if ch.isalpha():
       print("Alphabet")
    elif ch.isdigit():
       print("Digit")
    else:
       print("Special character")

ch = input("Enter a character: ")
check(ch)


