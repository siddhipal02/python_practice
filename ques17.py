
def countVowels(text, vowels):
    count = 0
    for ch in text:
       if ch in vowels:
         count += 1

    print("Number of vowels:", count)
text = "Hello World"
vowels = "aeiouAEIOU"
countVowels(text,vowels)
