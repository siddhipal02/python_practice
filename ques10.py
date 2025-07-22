def check(ch):
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    elif ch.isalpha():
        print("Consonant")
    else:
        print("Not an alphabet")

check('e')

