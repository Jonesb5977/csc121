#

num=int(input("Enter how many classes do you want to enter: "))
fname =str(input("Enter your first name: "))
lname=str(input("Enter your last name: "))
wname=fname.lower() + lname.lower()
with open("sechudale.txt","w") as outfile:
    for count in range(1,num +1):


       outfile.write(wname.ljust(20))
