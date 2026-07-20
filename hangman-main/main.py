import random

game_mode = input("Choose a game mode: (1) Two Player, (2) One Player: ")
while game_mode != "1" and game_mode != "2":
    game_mode = input("Invalid input." + "\n" + "Choose a game mode: (1) Two Player, (2) One Player: ")

word = ""
guesses = []
missed_guesses = []
hangman_stages = [
    """
      --------
      |      |
      |
      |
      |
      |
      =========""",
    """
      --------
      |      |
      |      O
      |
      |
      |
      =========""",
    """
      --------
      |      |
      |      O
      |      |
      |
      |
      =========""",
    """
      --------
      |      |
      |      O
      |     /|
      |
      |
      =========""",
    """
      --------
      |      |
      |      O
      |     /|\\
      |
      |
      =========""",
    """
      --------
      |      |
      |      O
      |     /|\\
      |      |
      |
      =========""",
    """
      --------
      |      |
      |      O
      |     /|\\
      |      |
      |     /
      =========""",
    """
      --------
      |      |
      |      O
      |     /|\\
      |      |
      |     / \\
      =========""",
]

f = open("placeholder", "r")
if game_mode == "1":
    word = input("Player 1, enter your word: ").lower()
    
elif game_mode == "2":
    difficulty = input("Choose a difficulty: (1) Easy, (2) Medium, (3) Hard: ")
    if difficulty == "1":
        # word = random.choice(easy_words)
        f = open("easy.txt", "r")
    elif difficulty == "2":
        # word = random.choice(medium_words)
        f = open("medium.txt", "r")
    elif difficulty == "3":
        # word = random.choice(hard_words)
        f = open("hard.txt", "r")
    else:
        print("Invalid dif v      ficulty choice.")
        while difficulty !="1" and difficulty !="2" and difficulty !="3":
            difficulty = input("Invalid input. Choose a difficulty: (1) Easy, (2) Medium, (3) Hard: ")

    words = []
    for line in f:
        words.append(line)
    
    x = random.randint(0, len(words)-1)
    word = words[x]
    word = word.strip()
print(word)
display_blanks = []
for i in range(0, len(word)):
    display_blanks.append("_")
    
condition = 0
while condition == 0:
    print(hangman_stages[len(missed_guesses)])
    print("Missed letters:", ",".join(missed_guesses))
    print("Current word:", " ".join(display_blanks))

    guess = input("Enter a letter or the whole word: ").lower()

    if len(guess) == len(word):
        if guess == word:
            print("You won! The word was", word)
            condition = 1
        else:
            print("Incorrect. The word was", word)
            missed_guesses.append(guess)
            
    elif len(guess) == 1:
        if guess in guesses:
            print("You already guessed that letter.")
        elif guess in word:
            print("Correct!")
            for i in range(len(word)):
                if word[i] == guess:
                    display_blanks[i] = guess
            guesses.append(guess)
        else:
            print("Incorrect. You are a loser.")
            missed_guesses.append(guess)
            guesses.append(guess)
    else:
        print("Invalid input. Please enter a single letter or the whole word.")

    if "_" not in display_blanks:
        print("You won! The word was", word)
        condition = 1