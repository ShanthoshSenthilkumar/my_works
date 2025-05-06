def marksheet():

    name=input("Enter the name of the student:")
    roll_no=int(input("Enter the rollno:"))
    Tamil=int(input("Enter the student's Tamil mark:"))
    English=int(input("Enter the student's English mark:"))
    Maths=int(input("Enter the student's Maths mark:"))
    Science=int(input("Enter the student's Science mark:"))
    Social=int(input("Enter the student's Social mark:"))

    Total=Tamil + English + Maths + Science + Social
    Average= Total / 500 * 100


    if(Tamil<40 or English<40 or Maths<40 or Science<40 or Social<40):
        print("Fail")
    else:
      if (Average>90 and Average<=100):
        print("A(Excellent)")
      elif (Average>80 and Average<=90):
         print("B(Very Good)")
      elif (Average>70 and Average<=80):
         print("C(Good)")
      elif (Average>40 and Average<=60):
         print("D(Pass)")
      else:
         print("F(Fail)")

    marksheet()
marksheet()
