"""Name: Joshua Bee son
<hw1.py>
Problem:f This program solves the issue of having to manually calculate several simple equations.
I certify that this assignment is entirely my own work."""
import math


def sum_of_threes():

    acc = 0
    threes = eval(input("Input the number you want to find the sum of threes of here: "))
    ran = int(threes / 3)
    for i in range(1, ran + 1):
        acc = acc + (i*3)
    print(acc)




def multiplication_table():
    for i in range(1,11):

        acc = i

        for num in range(1,11):
            maff = acc * num
            print(maff, end="\t")






def triangle_area():
    side_a = eval(input("Enter side a length "))
    side_b= eval(input("Enter side b length "))
    side_c = eval(input("Enter side c length "))
    triangle_s = (side_a + side_b + side_c) / 2
    triangle_a = math.sqrt(triangle_s * (triangle_s - side_a) *
                           (triangle_s - side_b) * (triangle_s - side_c))
    print("Area is ", float(triangle_a))



def sum_squares():
    lower = eval(input("Enter a Lower_bound "))
    upper = eval(input("Enter an Upper_bound"))
    acc = 0
    for i in range(lower, upper+1):
        this = i*i
        acc = acc + this
    print(acc)




def power():
    base = eval(input("Enter base: "))
    exponent = eval(input("Enter exponent: "))
    acc = base
    for _ in range(1, exponent):
        acc = acc * base

    print(acc)



if __name__ == '__main__':
    pass
