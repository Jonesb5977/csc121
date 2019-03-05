#Brandon Jones
#1/24/19
#JonesMainGP
#This program will calculate your net pay
import JonesFunctions as func
def main():
    func.displayinfo()
    HW=func.getHours()
    HR=func.getRate()
    GP=func.getGrossPay(HW,HR)
    SWT=func.getSWT(GP)
    FWT=func.getFWT(GP)
    NP=func.getNetPay(GP,SWT,FWT)
    func.displayValue(GP,SWT,FWT,NP)
    
    




if __name__ == "__main__":
    main()
