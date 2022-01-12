"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
from graphics import *



def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)



def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * height * width
    print(volume)



def shooting_percentage():
    total_shots = eval(input("Input the total shots taken: "))
    shots_made = eval(input("input the total shots made: "))
    shooting_percent = (shots_made/total_shots) * 100

    print(shooting_percent, " %")



def coffee():
    pounds = eval(input("How many pounds of coffee would you like?"))
    total_cost = float((10.50 * pounds) + (0.86 * pounds) + 1.5)
    print("Your total is: ", total_cost, "$")



def kilometers_to_miles():
    kilometers = eval(input("How many Kilometers did you travel? "))
    miles = round(float(kilometers / 1.61), 2)
    print("That's ", miles, " miles!")



if __name__ == '__main__':
    pass
