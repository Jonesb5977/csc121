#CW_27
#Demo how to throw exceptions
print ("Menu")
print ("1. Create textfile")
print ("2. Average Vales")
print ("3. Total value")
print ("4. Test for file exceptions")
print ("5. test for value error exception")
input (print("Enter your Choice: ")
##try:
##    num=int(input("Enter how many numbers you want to get from the user: "))
##
##    with open ("number.txt", "w") as outfile:
##        for count in range(1, num+1):
##            number=int(input("enter a number: "))
##            outfile.write(str(number)+ "\n")
##except ValueError:
##    print("incorrect entry. Entries should be integers!")

try:
    with open ("number.txt","r") as infile:
        total = 0
        count = 0
        for line in infile:
            value = int(line)
            count = count + 1
            total = total + value
        ave = total / count
        print(total)
        print(ave)
except ValueError:
    print("Bad data on line: " ,count + 1, sep="")
except IOError:
    print("Flie not found or conrupt")

    

