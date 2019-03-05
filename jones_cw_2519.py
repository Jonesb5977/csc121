#Brandon Jones
#2/5/19
#jones_cw_2519
#This program will gather a little information and put it into a file




num=int(input("Enter how many employees you want to enter: "))
with open ("pay.txt","w") as outfile:
    for count in range(1,num +1):
        fname=str(input("Enter employees first name: "))
        lname=str(input("Enter employees last name: "))
        wname=fname.lower() + lname.lower()
        title=str(input("Enter their title (salaried or hourly): "))
        prate=int(input("Enter the pay rate: "))
        hwork=int(input("Enter the hours they worked: "))
        gpay=prate*hwork


        outfile.write(wname.ljust(20) + title.ljust(10) + str(prate) + str(hwork) + str(gpay) + "\n")
