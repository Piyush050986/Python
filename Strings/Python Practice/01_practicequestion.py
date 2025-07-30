#  program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old
from datetime import datetime
age = int (input ("please enter your age "))
name = str(input ("please enter your name "))
age=100-age
current_year = datetime.now().year
age=current_year+age
print("you will turn 100 in the year ", age)


