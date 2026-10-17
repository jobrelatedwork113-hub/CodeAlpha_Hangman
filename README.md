CodeAlpha Hangman Game

About

This is a console-based Hangman game developed using Python as part of the CodeAlpha Python Programming Internship.

Features

- Random word selection
- Letter-by-letter guessing
- Six incorrect attempts allowed
- Input validation
- Prevents duplicate guesses
- Colorful console output

Technologies Used

- Python
- Random module
- VS Code

How to Run

1. Install Python.
2. Download "hangman.py".
3. Open a terminal in the file's folder.
4. Run:

python hangman.py

How to Play

1. Run the program.
2. Guess one letter at a time.
3. Correct guesses reveal letters in the word.
4. You win by guessing the complete word before running out of attempts.

output:
       Welcome to Hangman!
_ _ _ _ _ _ _ Attempts remaining: 6

Guess a letter:p
Correct guess!
_ P _ _ _ _ _ Attempts remaining: 6

Guess a letter:a
Correct guess!
_ P A _ _ _ _ Attempts remaining: 6

Guess a letter:e
Wrong guess!
_ P A _ _ _ _ Attempts remaining: 5

Guess a letter:c
Wrong guess!
_ P A _ _ _ _ Attempts remaining: 4

Guess a letter:n
Correct guess!
_ P A N _ _ _ Attempts remaining: 4

Guess a letter:e
You already guessed that letter!
_ P A N _ _ _ Attempts remaining: 4

Guess a letter:r
Wrong guess!
_ P A N _ _ _ Attempts remaining: 3

Guess a letter:h
Correct guess!
_ P A N _ _ H Attempts remaining: 3

Guess a letter:s
Correct guess!
S P A N _ S H Attempts remaining: 3

Guess a letter:i
Correct guess!
S P A N I S H Attempts remaining: 3
Congratulations! You guessed the word!
Thanks for playing Hangman!

Internship

Developed for the CodeAlpha Python Programming Internship.
