try:
    x=4
    y=int(input("enter the number:"))
    c=x/y
except ZeroDivisionError:
    print("ZeroDivisionError: please check input!")
else:
    print("thank you answer right")