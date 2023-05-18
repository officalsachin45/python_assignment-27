try:
    num=int(input("enter the integer number:"))
except ValueError:
    print("value error occurred. Please check your input.")
else:
    print(f"The square of {num} is {num**2}.")