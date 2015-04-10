'''
Created on Jan 24, 2015

@author: Zihang
'''
from random import randint

def checkNumbers(theGuessNumber):
    print("Type a number to guess!")
    while True:
        try:
            userGuess = int(input("Your input: "))
            if(userGuess == theGuessNumber):
                print("You have guessed correctly, and the program exists!")
                exit()
            else:
                if(userGuess > theGuessNumber):
                    print("It is greater than the guess")
                else:
                    print("It is less than the guess")
        except ValueError:
            print("Remember, you need to give a number!") 
                       
def GuessNumber():
    print("You need to guess a number between 1 and 100!")
    theGuessNumber = randint(1, 101)
    checkNumbers(theGuessNumber)

def main():
    print("This is a guess number game")
    GuessNumber()

if __name__ == "__main__":
    main()