"""Name: Joshua Bee son
<hw1.py>
Problem:f This program solves the issue of having to manually calculate several simple equations.
I certify that this assignment is entirely my own work."""


def name_reverse():
    name = input("enter a name (first last): ")
    new_name = name.replace(" ", ",")
    splitter = new_name.split(",")
    print("{lname}, {fname}".format(lname = splitter[1], fname = splitter[0]))


def company_name():
    cname = input("enter a domain: ")
    list = cname.split(".")
    print(list[1])


def initials():
    nstudents = eval(input("how many students are in the class? "))
    for i in range(nstudents):
        initial = []
        name = input("what is the name of student {i}?".format(i = i))
        new_name = name.split(" ")
        for text in new_name:
            letters = str(text)
            initial.append(letters[0])
        print("{f}{l}".format(f = initial[0], l = initial[1]))


def names():
    name = input("enter a list of names")
    list = name.split(" ")
    sublist = []
    for words in list:
        string = ""
        for letters in words:
            letter = letters.replace(' ', '').replace(',','')
            string = string + letter
        sublist.append(string)

    initial = []
    for text in sublist:
        letters = str(text)
        initial.append(letters[0])
    acc = 0
    print(initial)
    for i in range(2, len(initial)+1,2):
        for let in initial[acc:i]:
            print(let, end="")
        acc += 2




def thirds():
    num = eval(input("enter the number of sentences: "))
    final_list = []
    for i in range(1, num + 1):
        list_o_words = []
        sentence = input("enter sentence {i}: ".format(i = i))
        for text in range(0,len(sentence), 3):
            list_o_words.append(sentence[text])
        final_list.append(list_o_words)
    for length in range(0, num):
        list = final_list[length]
        for words in list:
            print(words, end="")
        print(end="\n")


def word_average():
    sen = input("enter a sentence: ")
    list = sen.split(" ")
    acc = 0
    for words in list:
        acc = acc + len(words)
    print(acc/len(list))


def pig_latin():
    sen = input("enter a sentence to convert to pig latin: ")
    list = sen.split(" ")
    final_list = []
    for words in list:
        words = words + words[0] + "ay"
        words = words.replace(words[0],'',1)
        words = words.lower()
        final_list.append(words)
    for words in final_list:
        print(words, end=" ")



if __name__ == '__main__':

    pass

