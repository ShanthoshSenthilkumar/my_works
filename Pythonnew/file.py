

def create_file():
    filename=input("Enter your filename:")
    filename=filename + ".txt"
    file=open(filename,"w")
    # file.write("The file name was created:" + filename + "\n")
    # file.write("Welcome to our file.\n")
    file.close()
    print(f"File'{filename}' has been created successfully")

def get_input():
    filename=input("Enter your filename:")
    file=open(filename + ".txt","w")
    content=input("Enter content to view in your file:")
    file.write(content)
    file.close()
    print("Successfully Added")


def use():
    User=int(input("Enter 1 for create file, Enter 2 for input:"))
    print(f"You choice:{User}")

    if(User==1):
        create_file()
        use()
    elif(User==2):
        get_input()
        use()
    else:
       print ("Invalid option")
use()






