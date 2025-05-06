import os  #access all files contains in a system

# os.mkdir("file_handling")  #creating a folder using python

# print("folder created")

# os.rmdir("file_handling")  #remove a folder

# fi=open("File_handling.txt","x")  #x-->refers create a file

a="Welcome to file handling"

fi=open("file_handling.txt","w") #w-->to write on a file
fi.write(a)
fi.close()

# fi=open("file_handling.txt","r")
# print(fi.read())
