import os

print(os.getcwd())# gets the current working directory

#Switching to some other directory
os.chdir("C:\\")
print(os.getcwd())

#create directoy
#os.mkdir("C:\\Users\\Elcot\\Desktop\\dummy")

#open and read a file
file_to_be_read=open("C:\\Users\\Elcot\\Desktop\\dummyText.txt")
message=file_to_be_read.read()
print(message)

#Writing to a file
file_to_be_written=open("C:\\Users\\Elcot\\Desktop\\dummyText1.txt","a")
file_to_be_written.write("Written by code")
file_to_be_written.write("This will be appended")
file_to_be_written.close()

