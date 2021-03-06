"""
The program will take in a list of grades from a final exam and process 
the data to output the amount of grades, average grades, and the percentage 
of grades that are above the average grade.
The first part will read the text file using infile and make the data into a list of strings to  be able to format
them from python. You then take the list and make it into integers.
Then for the first calculation, the lens command will read the amount of
strings in the list and set it equal to total grades variable.
The next command will find the average by calculting the sum of the list and dividing it by the len.
and finally you will need to calculate the amount of integers that are above the average by using a for/in command.

"""


"""
Under main function:

use infile to open up final.txt
define grades variable to final.exe and format it into a string
close infile
use a for in command to convert the string of numbers to integers
get the number of grades by using grade len command
get the average by dividing sum by len for grades
print grade lens
print  average
print above average / total grades * 100

Run Main function

define grades above average function
get the amount of scores that are above average by testing each number and seeing if its greater than average.

run grades above average function



"""


infile = open("Final.txt", 'r')
grades = [line.rstrip() for line in infile]
infile.close()
for all in range(len(grades)):
     grades[all] = int(grades[all])

averagegrade = sum(grades)/ len(grades)
grade = averagegrade

def main():

     print("Number of Grades:", len(grades))
     print("Average grade:", averagegrade)

def calculate_percent_above_average():
     test = 0 
     for avgtest in grades:
         if avgtest > averagegrade:
             test += 1
     Percentabove= (100 * test / len(grades))

     print("Percentage of grades above aveage: {0:.2f}%"
         .format(Percentabove))  
main()
calculate_percent_above_average()