#Brandon Jones
#2/12/19
#Jones_VanHoof_FE2
#this program will go off the menu for the options
def main():
    print ("Menu")
    print ("1. Create textfile")
    print ("2. Average Vales")
    print ("3. Total value")
    print ("4. Test for file exceptions")
    print ("5. Test for value error exception")
    print ("6. Exit the program")
    choice = int(input ("Enter your Choice: "))

    if (choice==1):
        num=int(input("Enter how many numbers you want to get from the user: "))

        with open ("numbers.txt", "w") as outfile:
            for count in range(1, num+1):
                number=int(input("enter a number: "))
                outfile.write(str(number)+ "\n")


    elif (choice==2):
         with open ("numbers.txt","r") as infile:
            total = 0
            count = 0
            for line in infile:
                value = int(line)
                count = count + 1
                total = total + value
            ave = total / count
            print(ave," is your average")

    elif(choice==3):
        with open ("numbers.txt","r") as infile:
            total = 0
            count = 0
            for line in infile:
                value = int(line)
                count = count + 1
                total = total + value
            print(total," is your total")

    elif (choice==4):
        try:
           with open ("numbers.txt","r") as infile:
                total = 0
                count = 0
                for line in infile:
                    value = int(line)
                    count = count + 1
                    total = total + value
        except IOError:
             print("File is not found or is corrupt")


        
    elif (choice==5):
        try:
            with open ("numbers.txt","r") as infile:
                total = 0
                count = 0
                for line in infile:
                    value = int(line)
                    count = count + 1
                    total = total + value
        except ValueError:
            print("Bad data on line: ", count + 1,sep=="")

    elif (choice==6):
        quit()

    else:
        input("Press enter to go back to the main menu")
        main()
main()
