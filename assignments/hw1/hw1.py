
"""Name: Joshua Bee son
<hw1.py>
Problem: This program solves the issue of having to manually calculate several simple equations.
I certify that this assignment is entirely my own work."""



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
    miles = float(kilometers / 1.61)
    print("That's ", miles, " miles!")



if __name__ == '__main__':
    pass
