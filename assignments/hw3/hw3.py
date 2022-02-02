"""Name: Joshua Bee son
<hw1.py>
Problem:f This program solves the issue of having to manually calculate several simple equations.
I certify that this assignment is entirely my own work."""


def average():
    grades = eval(input("how many grades will you enter? "))
    acc = 0
    for i in range(grades):
        enter = eval(input("Enter grade: "))
        acc = float(acc + enter)
    print("average is ", (acc/grades))



def tip_jar():
    acc = 0
    for i in range(5):
        money = eval(input("how much would you like to donate? "))
        acc = float(acc + money)
    print("total tips: ",acc)



def newton():
    num = eval(input("What number do you want to square root? "))
    improve = eval(input("How many times should we improve the approximation? "))
    approx = num
    for i in range(improve):
        approx = float(((approx + (num/approx))/2))
    print("the square root is approximately ", approx)


def sequence():
    terms = eval(input("how many terms would you like? "))
    list = []
    for i in range(1,terms + 1, 2):
        list.append(i)
        list.append(i)
    print(list[:terms])

def pi():
    term = eval(input("how many terms in the series?"))
    acc = 1
    for i in range(term):
        num = 2 + (i // 2 * 2)
        denom = 1 + ((i + 1) // 2 * 2)
        acc = acc * (num / denom)
    print(acc * 2)



if __name__ == '__main__':
    pass
