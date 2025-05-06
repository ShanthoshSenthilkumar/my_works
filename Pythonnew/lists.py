a=["Dhoni","Vijay","Raina"]
print(type(a))

# to insert in lists

a=["Dhoni","Ajith","Raina"]
# print(type(a))
a.append("Rutu")
print(a)
a.insert(1,"Vijay")
print(a)

# to update in lists

a=["Lexus","Volvo","BMW"]
print(a)
a[0]="Toyota"
print(a)

# to delete in lists
a=["Tata","Mahindra","Skoda"]
print(a)
a.pop(1)
print(a)
a.remove("Mahindra")
print(a)