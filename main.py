import random
from words import wordlist


def display_hangman(incorrect_guesses):
    hangman_graphics = [
        """

         -----
         |   |
             |
             |
             |
             |
        ------
        """
        ,
        """
        WRONG!
        
         -----
         |   |
         O   |
             |
             |
             |
        ------
        """
        ,
        """
        WRONG!
        
         -----
         |   |
         O   |
         |   |
             |
             |
        ------
        """
        ,
        """
        WRONG!
        
         -----
         |   |
         O   |
        /|   |
             |
             |
        ------
        """
        ,
        """
        WRONG!
        
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        ------
        """
        ,
        """
        WRONG!
        
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        ------
        """
        ,
        """
        WRONG!
        
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        ------
        """
    ]

    return hangman_graphics[incorrect_guesses]


def getValidWord(list):
    word = random.choice(list)
    while "-" in word or " " in word:
        word = random.choice(list)
    return word


def getIndex(word, letter):
    index = 0
    for char in word:
        if char == letter:
            print(index)
        index = index + 1


def blankword(word):
    blankw = ""
    for i in range(len(word)):
        blankw = blankw + "_"
    return blankw


def PLetterPlacement(Pword, letter):
    for i in range(len(word)):
        if word[i] == letter:
            Pword = Pword[:i] + letter + Pword[i + 1:]
    return Pword


print("              HANGMAN GAME")
print("")

chances = 6
incorrect_guesses = 0
word = getValidWord(wordlist)
blanks = blankword(word)
print(blanks)
print("")
print(display_hangman(incorrect_guesses))

while chances <= 6 and chances > 0:
    guesstype = input("Have you figured it out?(y for yes or n for no): ")
    if guesstype == "n":
        guessletter = input("Enter letter: ")
        if guessletter in word:
            Psword = ""
            index = 0
            for char in word:
                if char == guessletter:
                    Psword = PLetterPlacement(blanks, word[index])
                index = index + 1
            print(Psword)
            blanks = Psword
            if blanks == word:
                print("Congratulations!You Won")
                break
        else:
            incorrect_guesses+=1
            print(display_hangman(incorrect_guesses))
            chances = chances - 1
            if chances != 0:
                print(f"Guess again,{chances} guesses remaining.")
            else:
                print("Hangman!You are out of guesses")
                print(f"The word was '{word}'")

    elif guesstype == "y":
        guessword = input("Enter word: ")
        if guessword == word:
            print("Congratulations!You Won")
            break
        else:
            print("Incorrect word!")
            incorrect_guesses+=1
            print(display_hangman(incorrect_guesses))

            chances = chances - 1
            print(f"Guess again,{chances} guesses remaining.")
    else:
        print("INVALID INPUT!")