try:
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    c=a/b
except ValueError:
    print("cheak the value:")
except ZeroDivisionError:
    print("value error please cheak input")
except Exception as e:
    print("an error occuay:",str(e))
else:
    print("No exceptions were raised")
finally:
    print("the code always execute")