import random
# Text colours
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
PURPLE = "\033[95m"
RESET = "\033[0m"
words=["SPANISH","FEATHER","CODING","PYTHON","PLASTIC"]
secret_word=random.choice(words)
guessed_letters=[]
all_guesses=[]
max_attempts=6
wrong_attempts=0
print(CYAN + "Welcome to Hangman!" + RESET)
while wrong_attempts<max_attempts:
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print(YELLOW + "Attempts remaining: " +
      str(max_attempts - wrong_attempts) + RESET)
    if all(letter in guessed_letters for letter in secret_word):
        print(GREEN + "Congratulations! You guessed the word!" + RESET)
        break
    guess=input("\nGuess a letter:").upper().strip()
    if len(guess)!=1 or not guess.isalpha():
        print(YELLOW + "Please enter only one alphabet." + RESET)
        continue
    if guess in all_guesses:
        print(YELLOW + "You already guessed that letter!" + RESET)
        continue
    all_guesses.append(guess)
    if guess in secret_word:
        guessed_letters.append(guess)
        print(GREEN + "Correct guess!" + RESET)
    else:
        wrong_attempts+=1
        print(RED + "Wrong guess!" + RESET)
else:
    print(RED + "\nGame over! You ran out of attempts." + RESET)
    print(YELLOW + "The correct word was: " + RESET + RED + secret_word + RESET)
print(CYAN + "Thanks for playing Hangman!" + RESET)
       