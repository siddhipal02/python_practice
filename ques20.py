def checkPalindrome(word):
    rev = word[::-1]
    if rev == word:
        print("Palindrome")
    else:
        print("Not Palindrome")

text = "nun"
checkPalindrome(text)


