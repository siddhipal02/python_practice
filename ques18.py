a = 10
b = 5
op = '+'

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
