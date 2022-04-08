"""Name: Joshua Bee son
<hw1.py>
Problem: this does math
I certify that this assignment is entirely my own work."""
from sphere import Sphere


def fibonacci(num):
    # My idea is we have two accumulators, obviously
    # the number of times we run the program is equal to nth number.
    # Acc = list[-1] and Acc1 = list[-2] acc + acc1 = list.apppend()
    # | the list gets updated and rinse and repeat.
    list = [0,1]
    if num > 0:
        # I have no idea why it needs to be one.
        # I set it to greater than zero so as soon as it reach
        # 0 it would stop. Why does that not work?1?!
        while num > 1:
            num -= 1
            acc = list[-1]
            acc1 = list[-2]
            acc3 = acc + acc1
            list.append(acc3)
        return list[-1]



def double_investment(principle, rate):
    # my idea here is I take the principle and I set
    # another value equal to double the principle value.
    principle_2 = principle * 2
    acc = 0
    while (principle or A) < principle_2:
        acc+= 1
        A = principle * (1 + rate)
        principle = A
    return acc


def syracuse(num):
    list = [num]
    while (num/2) != 1:
        if (num%2) == 0:
            num = num / 2
            list.append(int(num))
        elif (num%2) != 0:
            num = (num * 3) + 1
            list.append(int(num))
    list.append(1)
    return list


def create_prime(n):
    num_acc = 2
    num_list = []
    while num_acc != n:
        num_list.append(num_acc)
        num_acc += 1
    while_acc = 0
    num_list.append((num_list[-1] + 1))
    prime_list = []
    f = False
    while num_list[while_acc] < num_list[-1]:
        num = num_list[while_acc]
        nest_acc = 0
        while num_list[nest_acc] != num:
            nest_num = num_list[nest_acc]
            if (num % nest_num) == 0:
                f = False
                break
            else:
                f = True
            nest_acc += 1
        if f:
            prime_list.append(num)
        while_acc += 1
    return prime_list


def goldbach(n):
    # check all numbers < n to see if they are prime, if they are add them to a list.
    # Then loop through said list and WHILE list[acc] != list[-1]: keep looping through.
    # if the while loop goes through the entire list return None (this won't be possible in this case) else we
    # return the two numbers in a list format
    # thinking through after we make the list of prime numbers we will have to have another list with all
    # the prime numbers and multiple the current prime number by each prime number in the second list,
    # or we could use the original list maybe? yeah I can do that I think. we'll see
    if (n%2) == 0:
        prime_list = create_prime(n)
        ret_list = []
        acc = 0
        while acc < len(prime_list):
            num = prime_list[acc]
            nest_acc = 0
            while nest_acc < len(prime_list):
                nest_num = prime_list[nest_acc]
                if (num + nest_num) == n:
                    ret_list.append(num)
                    ret_list.append(nest_num)
                    return ret_list
                nest_acc += 1
            acc += 1
    else:
        return None
def hello(radius):
    circle = sphere(radius)
    print(circle.volume(), circle.get_radius(), circle.surface_area())

