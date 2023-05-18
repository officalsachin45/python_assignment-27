try:
    a=9
    b=int(input("enter the without using zero: "))
    c=a/b
except ArithmeticError:
    print("An arithmetic error occurred. Please check your input.")
else:
    print("oaky your right")