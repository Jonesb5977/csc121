#Brandon Jones
#1/24/19
#JonesMainGP
#This program is all the functions

def displayinfo():
    print("Brandon Jones")
    print("This program will calculate your netpay.")

#HW=HoursWorked
def getHours():
    HW=float(input("Enter how many hours you work "))
    return HW
#HR=HourlyRate
def getRate():
    HR=float(input("Enter your hourly rate "))
    print()
    print()
    return HR


#GP=GrossPay
def getGrossPay(HW,HR):
    GP=HW*HR
    return GP

def getSWT(GP):
    SWT=.01*GP
    return SWT

def getFWT(GP):
    FWT=.02*GP
    return FWT

#NP=NetPay
def getNetPay(GP,SWT,FWT):
    NP=GP-(SWT+FWT)
    return NP

def displayValue(GP,SWT,FWT,NP):
    print(GP," is your grossPay")
    print()
    print(FWT, " is your Federal withholding")
    print()
    print(SWT, " is the state withholding")
    print()
    print(NP, " is your netpay")
    
    
