try:
    a=8
    b=int(input("enter the number:"))
    if a==b:
        raise ArithmeticError()   
    c=a/b
except ArithmeticError:
    print("Arithmetic error occurred")



