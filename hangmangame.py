import random

print("Bienvenu dans mon jeu Hangman")
print("-------------------------------------------------------")


worldDictionary = ["sunflower","dar","diamond","meme","chose","hello","cute","belle","bureau"]


# choisir un ramdom mot
randomword =random.choice(worldDictionary)

for x in randomword:
    print("_",end=" ")


def print_hangman(wrong):
    if(wrong == 0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 1):
        print("\n+---+")
        print("o   |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 2):
        print("\n+---+")
        print("o   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif(wrong == 3): 
        print("\n+---+")
        print(" o  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif(wrong == 4):
        print("\n+---+")
        print(" o  |")
        print("/|\ |")
        print("    |")
        print("   ===") 
    elif(wrong == 5): 
        print("\n+---+")
        print(" o  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif(wrong == 6): 
        print("\n+---+")
        print(" o  |")
        print("/|\ |")
        print("/ \ |")
        print("   ===")    


def printword(guessdLetters):
    counter=0
    rightLetters=0
    for char in randomword:
        if(char in guessdLetters):
            print(randomword[counter],end=" ")
        else:
            print(" ",end=" ")
        counter+=1
        return rightLetters
    

def printLines():
    print("\r")
    for char in randomword:
        print("\u203E", end=" ")


length_of_word_to_guess = len(randomword)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while(amount_of_times_wrong !=6 and current_letters_right!= length_of_word_to_guess):
    print("\nLetters guessed so far :")
    for letter in current_letters_guessed:
        print(letter, end=" ")
    letterGuessed =input("\nGuess a letter :")
    # if correct:
    if(randomword[current_guess_index]==letterGuessed):
        print_hangman(amount_of_times_wrong)
        current_guess_index +=1
        current_letters_guessed.append(letterGuessed)
        current_letters_right=printword(current_letters_guessed)
        printLines()
    else:
        amount_of_times_wrong+=1
        current_letters_guessed.append(letterGuessed)
        print_hangman(amount_of_times_wrong)
        current_letters_right = printword(current_letters_guessed)
        printLines()

print("Game over !")
