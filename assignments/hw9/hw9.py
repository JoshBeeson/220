from random import randint
from graphics import *


def get_words(file_name):
    in_file = open(file_name, "r")
    word_list = []
    for line in in_file:
        word_list.append(line)
    return word_list


def get_random_word(words):
    num = len(words) - 1
    rand = randint(0, num)
    word = str(words[rand])
    word = word.replace("\n", "")
    return word


def letter_in_secret_word(letter, secret_word):
    x = False
    for s_letter in secret_word:
        if ord(letter) == ord(s_letter):
            x = True
            break
        else:
            x = False
    return x


def already_guessed(letter, guesses):
    x = False
    for letters in guesses:
        if letter == letters:
            x = True
            break
        else:
            x = False
    return x


def make_hidden_secret(secret_word, guesses):
    # if we check if it is equal we either add the space and text or we add a space and underscore
    word = []
    char_list = []
    acc = 0
    s = ""

    for letter in secret_word:
        char_list.append(letter)
    for num in secret_word:
        word.append("_")
    for letter in guesses:
        for char in char_list:
            if letter == char:
                word[acc] = char
            acc += 1
        acc = 0
    for char in word:
        s = s + " " + char
    s = s.replace(" ", "", 1)
    return s


def won(guessed):
    for char in guessed:
        if char == "_":
            return False
    else:
        return True


def play_graphics(secret_word):
    # Window Building
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 100
    height = 100
    win.setCoords(0, 0, width, height)
    guessed = []
    g_left = 6

    # game
    while won is not True and g_left != 0:

        # GUI Building

        # drawing the pole
        base = Line(Point(20,20), Point(40,20))
        base.draw(win)

        pole = Line(Point(30,20), Point(30,60))
        pole.draw(win)

        pro = Line(Point(30,60), Point(50,60))
        pro.draw(win)

        hang = Line(Point(50,60), Point(50, 55))
        hang.draw(win)

        cur = make_hidden_secret(secret_word, guessed)

        # drawing current word
        current = Text(Point(50, 20), cur)
        current.draw(win)

        # drawing guessed word and the entry object
        guess = Text(Point(20, 10), guessed)
        guess.draw(win)

        entry = Entry(Point(50, 10), 1)
        entry.draw(win)
        win.getMouse()
        user = entry.getText()

        # Game Info
        if already_guessed(user, guessed) is False:
            guessed.append(user)
            if letter_in_secret_word(user, secret_word) is False:
                g_left -= 1
        cur = make_hidden_secret(secret_word, guessed)
        current.undraw()
        current.draw(win)

        # drawing the hangman
        if g_left == 5:
            head = Circle(Point(50, 50), 5)
            head.draw(win)
        if g_left == 4:
            torso = Line(Point(50, 45), Point(50, 30))
            torso.draw(win)
        if g_left == 3:
            arm = Line(Point(50, 44), Point(55, 38))
            arm.draw(win)
        if g_left == 2:
            arm_2 = Line(Point(50, 44), Point(45, 38))
            arm_2.draw(win)
        if g_left == 1:
            leg = arm.clone()
            leg.move(0, -12)
            leg.draw(win)
        if g_left == 0:
            leg_2 = arm_2.clone()
            leg_2.move(0, -12)
            leg_2.draw(win)

        # undraw Everything
        entry.undraw()
        guess.undraw()
        current.undraw()

        # checking win condition
    if won(cur) is True:
        win = Text(Point(50, 90), "winner!")
        win.draw(win)
        word = Text(Point(20, 10), secret_word)
        word.draw(win)
    if won(cur) is not True:
        loss = Text(Point(50, 90), "sorry, you did not guess the word.")
        loss.draw(win)
        loss_2 = loss.clone()
        loss_2.move(0,-5)
        loss_2.setText("the secret word was " + secret_word)
        loss_2.draw(win)
        current.draw(win)

    win.getMouse()
    win.close()


def play_command_line(secret_word):
    guessed = []
    g_left = 6

    while won is not True and g_left != 0:
        cur = make_hidden_secret(secret_word, guessed)
        print("already guessed: ", guessed)
        print("guesses remaining: ", g_left)
        print(cur)
        user = input("guess a letter: ")
        print(user)
        if already_guessed(user, guessed) is False:
            guessed.append(user)
            if letter_in_secret_word(user, secret_word) is False:
                g_left -= 1

    if won(cur) is True:
        print("winner!")
        print(secret_word)
    if won(cur) is not True:
        print("sorry, you did not guess the word.", "\n the secret word was " + secret_word)


    pass


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
