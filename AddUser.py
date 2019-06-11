import os
def chknum(name):
	return any(char.isdigit() for char in name)
name=input("Enter your name : ")
if not chknum(name):
	password="Hello"+name
	command="useradd -p $(openss1 passwd -1 "+password+")"+name
	os.system(command)
else:
	print("Error creating user")
