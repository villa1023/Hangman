from words import word_list
from words import hard_word_list
import random


def getWord():
    word = random.choice(word_list)
    return word.upper()


def getHardWord():
    word = random.choice(hard_word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    tries = 6
    print("Welcome to Hangman!")
    print(displayHangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetters:
                print("Letter ", guess, " has been already guessed!")
            elif guess not in word:
                print(guess, " is not in the word")
                tries -= 1
                guessedLetters.append(guess)
            else:
                print("Good job! ", guess, " is in the word")
                guessedLetters.append(guess)
                wordAsList = list(word_completion)
                indces = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in indces:
                    wordAsList[index] = guess
                word_completion = "".join(wordAsList)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess != word:
                print("You already guessed the word ", guess)
                tries -= 1
                guessedWords.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Not a valid guess.")
        print(displayHangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats! You guessed the word!")
    else:
        print("Sorry, you ran out of tries. The word was " +
              word + ". Better luck next time!")


def displayHangman(tries):
    stages = ["""
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                -     
    """,
              """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / 
                -     
    """,
              """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     
                -     
    """,
              """
                --------
                |      |
                |      O
                |     \\|
                |      |
                |     
                -     
    """,
              """
                --------
                |      |
                |      O
                |      |
                |      |
                |     
                -     
    """,
              """
                --------
                |      |
                |      O
                |     
                |      
                |     
                -     
    """,
              """
                --------
                |      |
                |      
                |     
                |      
                |    
                -     
    """
              ]
    return stages[tries]


def main():
    difficulty = input("Would you like to play easy or hard? E/H: ").upper()
    if difficulty == 'H':
        word = getHardWord()
        play(word)
    elif difficulty == 'E':
        word = getWord()
        play(word)
    while input("Play again? Y/N: ").upper() == "Y":
        difficulty = input(
            "Would you like to play easy or hard? E/H: ").upper()
    if difficulty == 'H':
        word = getHardWord()
        play(word)
    elif difficulty == 'E':
        word = getWord()
        play(word)


if __name__ == "__main__":
    main()
