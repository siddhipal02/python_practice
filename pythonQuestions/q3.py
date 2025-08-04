def palindrome(word):
    word = word.lower()
    return word[::-1] == word

word = input("enter a word: ")
is_palindrome = palindrome(word)
if is_palindrome == True:
    print("palindrome")
else:
    print("Not a palindrome")