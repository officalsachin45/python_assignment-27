try:
    n=int(input("enter the number:"))
    try:
        n1=int(input("enter the number:"))
        num=n/n1
    except ValueError:
        print("value error")
    except ZeroDivisionError:
        print("cannot divided by zero:")
    except Exception as e:
        print(str(e))
    else:
        print("valid code")
    finally:
        print("inner try block execution")
except ValueError:
    print("Please enter a valid integer for the first number.")
except Exception as e:
    print("An error occurred: ", str(e))
else:
    print("No exceptions were raised in the outer try block.")
finally:
    print("Outer try block executed.")