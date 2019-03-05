#Brandon Jones
#2/26/19
#Jones_M3P2
#This program willl tell you how many time a patiular team has won the world series

def main():        
    f = open ("WorldSeriesWinners.txt","r")

    teams=f.read()
    num=int(input("Enter how many teams you would like to check: "))
    for count in range (1,num+1):
    #get a name from the user
        name=input("Enter a team name: ")
        name= name.title()
    #count the times the team won
        count=teams.count(name)
        print(count, "is how many times the team won from 1903 to 2009")



main()
