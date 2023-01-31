#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

high_score = 95 #modified the case to match the var name in conditional statement below
 
# Get the test scores. 
##modified input to be float format as default is string. 
#Current configuration not able to handle user input error so modified with try except else stmt
try:
    test1 = float(input('Enter the score for test 1: '))
    test2 = float(input('Enter the score for test 2: '))
    test3 = float(input('Enter the score for test 3: ')) #missing the third test input
except:
    print('Please try again as the inputs could not be used. Please submit a numeric input')
# Calculate the average test score.
else:
    average = (test1 + test2 + test3) / 3 #added parentheses as division comes before addition in order of operations
    # Print the average.
    print('The average score is', average)
    # If the average is a high score,
    # congratulate the user.
    if average >= high_score:
        print('Congratulations!')
        print('That is a great average!') #modified the indentation to only print with high score averages

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 
try:
    rec_len1 = float(input('Enter the length of rectangle 1: '))
    rec_wid1 = float(input('Enter the width of rectangle 1: '))
    rec_len2 = float(input('Enter the length of rectangle 2: '))
    rec_wid2 = float(input('Enter the width of rectangle 2: '))
except:
    print('Incorrect input provided for rectangle dimensions. Please input a numeric value')
else:
    
    print(f'The area of Rectangle 1 is: {rec_len1 * rec_wid1}')
    print(f'The area of Rectangle 2 is: {rec_len2 * rec_wid2}')
#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

name = input('Please input your name: ')
age = int(input('Please input your age: '))


#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"
print(f'Happy Birthday, {name}! You are {age} years old today! You are getting old')