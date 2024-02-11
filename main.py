import random

game_title = 'Mr. Word'
word_bank = []

with open('words.txt') as word_file:
    for line in word_file:
        word_bank.append(line.rstrip().lower())

word_to_guess = random.choice(word_bank)

misplaced_guesses = []
incorrect_guesses = []
max_turns = 5
turns_taken = 0

# Introduce

print('Welcome to', game_title)
print('The word has', len(word_to_guess), 'letters.')
print('You have', max_turns - turns_taken, 'turns left.')

# Game loop

while turns_taken < max_turns:
    # Get player's guess
    guess = input('Guess a word: ').lower()

    # Check if the guess length equals 5 letters and is all alpha letters 
    if len(guess) != len(word_to_guess) or not guess.isalpha():
        print('Please enter 5-letter word.')
        continue

    # Check each letter in the guess against the word's letters
    index = 0
    for check_letter in guess:
        if check_letter == word_to_guess[index]:
            print(check_letter, end=' ')
            if check_letter in misplaced_guesses:
                misplaced_guesses.remove(check_letter)
        elif check_letter in word_to_guess:
            if check_letter not in misplaced_guesses:
                misplaced_guesses.append(check_letter)
            print('_', end=' ')
        else:
            if check_letter not in incorrect_guesses:
                incorrect_guesses.append(check_letter)
            print('_', end=' ')
        index += 1
    
    print('\n')
    print('Misplaced letters:', misplaced_guesses)
    print('Incorrect letters:', incorrect_guesses)
    turns_taken += 1

    # Check if the player has won
    if guess == word_to_guess:
        print('Congratulations, you win!')
        break
    if turns_taken == max_turns:
        print('Sorry, you lost. The word was', word_to_guess)
        break

    print('You have', max_turns - turns_taken, 'turns left.')