'''
Created on Jan 24, 2015

@author: Zihang
'''

from random import randint

def rollingDice(min = 1, max = 7):
    randomNumber = randint(min, max)
    print(randomNumber)
    
def main():
    rollingDice(1,7)
    while 1:
        try:
            i = int(input("If you want to roll the dice again, enter any number except 1 and press: "))  
            if(i == 1):
                print("You have typed a 1, program exists!")
                exit()
            rollingDice(1,7)    
        except ValueError:
                print("Oop, I said a number, type again!")
                
if __name__ == "__main__":
    main()
    