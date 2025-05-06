try:
    file=open("myfile.txt", "r")
    content=file.read()
except FileNotFoundError:
    print("File is not found")
except:
    print("Enter the proper file name.")
finally:
    print("File read successfully")


try:
    x=int(input("Enter a number:"))
    result=10/x
    print(result)
except ZeroDivisionError:
    print("you can't divide by zero")
except ValueError:
    print("That's not a valid number")
finally:
    print("Code runned")

