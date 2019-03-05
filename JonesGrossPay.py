#Brandon Jones
#1/22/19
#GrossPay_Jones
#This program will calculate the gross pay for an user
print("Brandon Jones")
print("This program will calculate your netpay from your gross payand taxes")
print()
#R is the hourly rate you make 
R=float(input("Enter your hourly rate "))
#H is the hours you work 
H=float(input("Enter how many hours you work "))
print()
FWT=.02
SWT=.01
#Calculation
#GP is the grosspay
GP=R*H
f=GP*FWT
s=GP*SWT
NP=GP-(s+f)
print(GP," is your grossPay")
print()
print(f, " is your Federal withholding")
print()
print(s, " is the state withholding")
print()
print(NP, " is your netpay")
