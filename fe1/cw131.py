#Brandon Jones
#1/31/19
#jonesFE1.py
#This is the program to run the sechudale file


num=int(input("Enter how many classes do you want to enter: "))
fname =str(input("Enter your first name: "))
lname=str(input("Enter your last name: "))
wname=fname.lower() + lname.lower()
with open("sechudale.txt","w") as outfile:
    for count in range(1,num +1):
        cname = str(input("Enter your class name: "))
        cname =cname.lower()
        mdays=str(input("Enter the days your class meets (m,t,w,th,f): "))
        mdays=mdays.lower()
        eTime=str(input("Enter the class end time: "))
        sTime=str(input("Enter the class start time: "))


        outfile.write(wname.ljust(20)+ cname+ mdays.ljust(6) + sTime + eTime +  "\n")
