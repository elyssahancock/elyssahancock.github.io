#Imports : 
from words import new_words_list
import random
#from tkinter import *
#from tkinter import ttk

def main():
    selected_word =choose_random_word()
    list_of_letters = list(selected_word)
    guessed_letters = []
    number_of_guesses = 0
    #lives = 5
    asterick_list = create_asterick_lists(list_of_letters)
    guess_a_letter(list_of_letters, asterick_list, guessed_letters, number_of_guesses, selected_word)

def choose_random_word():
    selected_word = random.choice(new_words_list)
    #print(selected_word)
    return selected_word

def create_asterick_lists(character_list):
    asterick_list = []
    for _ in range(len(character_list)):
        asterick_list.append("*")
    return asterick_list

def guess_a_letter(list_of_letters, asterick_list, guessed_letters, number_of_guesses, selected_word):
    while "*" in asterick_list: 

        guess = input("Guess a Letter: ").lower()
        number_of_guesses += 1
        if guess == "give up":
            print(selected_word)
            print(f"Guesses : {number_of_guesses}")
            break

        if guess in list_of_letters:
                print("Letter in word")
                #index_of_letter = list_of_letters.index(guess)
                index_of_letter = [i for i, j in enumerate(list_of_letters) if j == guess]
                for item in index_of_letter:
                    asterick_list[item] = guess 
        else:
            if guess in guessed_letters:
                None
            else:
                guessed_letters.append(guess)
                guessed_letters = sorted(guessed_letters)

        print()    
        print(f"\033[1m {asterick_list} \033[0m")
        print(f"Guessed Letters: {guessed_letters}")
    print()
    print(f"Guesses = {number_of_guesses}")
    print(selected_word)


main()