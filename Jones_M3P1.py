#Brandon Jones
#2/26/19
#Jones_M3P1
#This program will find the highest,lowest,average,and total of a set of data

def main():
    num=int(input("Enter how many numbers you would like to enter: "))
    my_list=[0]*num
    for index in range(num):
        number=int(input("Enter a value: "))
        my_list[index]=number
        ave=sum(my_list)/num
    print(my_list)
    print(max(my_list), "is the highest number")
    print(min(my_list), "is the lowest number")
    print(sum(my_list), "is the total of the list")
    print(ave, "is the average of the list")
    
main()
