# Word game

Our word-guessing game will prompt the player to guess a 5-letter word. As the player submits their word guess, the game will provide some feedback as to whether the letters within their guess are in the word to guess.

## How to play
If the player guesses the correct letter in the correct position, that letter will be filled in on the console. If they guess a correct letter that belongs in the word, but it is in the wrong position, that letter will be added to a list of misplaced letters, and an underscore will be shown in that position on the console. If they guess an incorrect letter that does not belong in the word, that letter will be added to a list of incorrect letters, and an underscore will be shown in that position on the console. The user will have a maximum of 5 tries to guess the word.

### Example
Guessed word: LIONS
Your word: LINKS
Output:
```
l i _ _ s
Misplaced letters: ['n']
Incorrect letters: ['k']
You have 4 turns left.
```
