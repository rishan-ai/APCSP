from wordlist import words, allowed_guesses
import random

guesses = 0
color_list = []
word = random.choice(words).lower()

def repetition_checker_word(word, character):
    counter = 0
    for i in range(len(word)):
        if character == word[i]:
            counter += 1
    return counter

def repetition_checker_guess(guess, character):
    counter = 0
    for i in range(len(guess)):
        if character == guess[i]:
            counter += 1
    return counter

def check_letter(word, guess):
    color_list = []
    for i in range(5):
        character = word[i]

        if word[i] == guess[i]:
            color_list.append("🟩")
        elif guess[i] not in word:  
            color_list.append("⬜")
        else:
            if repetition_checker_guess(guess, character) <= repetition_checker_word(word, character):
                if guess[i] in word and guess[i] != word[i]:
                    color_list.append("🟨")
                else:
                    color_list.append("⬜")
    return(color_list)
    # Sources used for the if statement in the third else statement in check_letter(word, guess)
    # Microsoft copilot https://copilot.microsoft.com

def win(word, guess):
    if word == guess:
        print("You won!")
        return True
    return False

while guesses < 6:
    guess = input("What word do you guess: ").lower()
    while len(guess) != 5 or (guess not in words and guess not in allowed_guesses):
        if len(guess) != 5:
            print("Word has to have 5 letters")
        else:
            print("Word not in wordlist")
        guess = input("What word do you guess: ").lower()

    guesses += 1

    print(check_letter(word, guess))

    if win(word, guess):
        break

    if guesses == 6 and not win(word, guess):
        print(f"You lost, the word was {word}")

