def reverse(str):
    words= str.split(" ")
    rev=words[::-1]
    return " ".join(rev)

str="hello world"
print(reverse(str))

