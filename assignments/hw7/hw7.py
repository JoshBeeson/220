
from encryption import encode, encode_better
def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, 'r')
    inf = infile.readlines()

    out = open(out_file_name, 'w')

    i = 0
    for line in inf:
        new_line = line.split()
        for word in new_line:
            i += 1

            print(str(i) + " " + word, file=out)




    infile.close()
    out.close()


def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, 'r')
    inf = infile.readlines()

    out = open(out_file_name, 'w')

    for line in inf:
        new_line = line.split(" ")
        new_line[2] = str(float(new_line[2]) + 1.65)
        wages = float(float(new_line[3]) * float(new_line[2]))
        print("{first} {last} {Wages:.2f}".format(first = new_line[0], last = new_line[1], Wages = wages) , file=out)

    infile.close()
    out.close()



def calc_check_sum(isbn):

    isbn = isbn
    acc = 10
    sum = 0
    for i in range(len(isbn)):
        try:
            num = int(isbn[i]) * acc

            sum = sum + num
            acc -= 1

        except:
            print('')

    return sum



def send_message(file, friend):
    infile = open(file, 'r')


    out = open('{friend}.txt'.format(friend=friend), 'w+')

    for line in infile.readlines():

        print(line,end="", file=out)

    infile.close()
    out.close()


def send_safe_message(file, friend, key):
    infile = open(file, 'r')

    out = open('{friend}.txt'.format(friend = friend), 'w', encoding="utf-8")

    for line in infile:
        lin = line.strip("\n")
        char = ""
        for c in lin:

            nc = encode(c, key)
            char += nc
        print(char, file=out)

    infile.close()
    out.close()


def send_uncrackable_message(file, friend, pad):
    infile = open(file, 'r')


    out = open('{friend}.txt'.format(friend = friend), 'w')


    padfile = open(pad, 'r')
    pad2 = padfile.readline()
    print(pad2)

    for line in infile:
        new = line.strip("\n")
        new_line = encode_better(new, pad2)
        print(new_line, file=out)

    infile.close()
    out.close()




if __name__ == '__main__':
    pass
