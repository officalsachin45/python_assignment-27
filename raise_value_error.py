def vailed_day(age):
    if age<0:
        raise ValueError("age cannot be negative")
    if age>70:
        raise ValueError("age can be greater than 70")
    else:
        print("valid age")
try:
    vailed_day(60)
except ValueError as e:
    print(str(e))