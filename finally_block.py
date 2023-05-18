try:
    a=9
    b=int(input("enter the number:"))
    c=a/b
    
    
except ZeroDivisionError:
    print("zerodivisionerror please check your input:")

finally:
    print("The 'try except' block is finished") 