print("Enter 1 for home, 2 for Industry,3 for Commercial")
user=int(input("Press the number:"))

a=int(input("Enter Previous Unit:"))
b=int(input("Enter Current Unit:"))

def home():
    total=b-a
    print("Total units:",total)
    if(total<=100):
        print("Free")
    else:
        print("Bill amount:",(total-100)*2)


def industry():
       total=b-a
       print("Total units:",total)
       print("Bill amount:",5*total)

def commercial():
       total=b-a
       print("Total units:",total)
       print("Bill amount:",2*total)


if (user==1):
    home()
elif(user==2):
    industry()
elif(user==3):
    commercial()
else:
    print("Invalid Option")


    
   