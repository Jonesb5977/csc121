#Brandon Jones
#2/14/19
#jones_handsonexam
#This program will collect data from different departments

num=int(input("Enter how many departments you would like to enter: "))
with open("Department item.txt","w") as outfile:
        for count in range(1,num+1):
            dname=str(input("Enter the department name: "))
            dname=dname.lower()
            dcode=str(input("Enter the department code: "))
            item=str(input("Enter the item name: "))
            item=item.lower()
            qty=str(input("Enter how many you have on hand: "))
            price=float(input("Enter how much the item cost: "))
            price=price*100
            price=int(price)

            outfile.write(dname.ljust(10) + dcode.ljust(4) + item.ljust(20) + qty.ljust(3) + str(price).ljust(4) +"\n") 
