# 🎮 Hangman Game Challenge

## 🎯 Objective

Build a command-line Hangman game to practice string manipulation, loops, conditionals, and handling user input.

## 📝 Tasks

### 🛠️ Build the Hangman Game

#### Description
Implement a playable Hangman game that runs in the terminal. The program should choose a secret word and allow the player to guess letters until they either reveal the whole word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Display the current word progress with unguessed letters shown as underscores (for example: `_ a _ _ a`)
- Accept single-letter guesses (case-insensitive) and reveal matching letters
- Track and display the number of incorrect attempts remaining
- Do not penalize repeated correct guesses
- End the game with a clear win or lose message and reveal the secret word
- Include a short list of example words in the code (or an external data file)

#### Example
```plaintext
Secret word: _ a _ _ a
Guess a letter: n
Correct! Current word: _ a n _ a
Incorrect guesses left: 5
```

