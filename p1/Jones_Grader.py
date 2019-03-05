#Brandon Jones
#1/22/19
#Jones_grader
#This program will calculate the grade average
import Jones_Grade_Functions
# main function that will do all of the functions calls
def main():
# function call and return # of grades to enter
    num = Jones_Grade_Functions.get_input()
# function call and return average
    average = Jones_Grade_Functions.get_average(num)
# function call and return letter grade
    letter_grade = Jones_Grade_Functions.get_letter_grade(average)
# function call to print letter grade
    Jones_Grade_Functions.display_grade(average,letter_grade)



if __name__ == "__main__":
    main()
