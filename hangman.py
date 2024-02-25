
 #Hang man/ compare the letters
import random
# stages for the hanged man
hangman_stages = ["""
    +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
==========
    
    YOU LOST!
    """, """
    +---+
     |   |
     O   |
    /|\  |
    /    |
         |
==========
    """, """
    +---+
     |   |
     O   |
    /|\  |
         |
         |
==========
    ""","""
    +---+
     |   |
     O   |
    /|   |
         |
         |
==========
    """, """
    +---+
     |   |
     O   |
         |
         |
         |
==========
    """, """
    +---+
     |   |
         |
         |
         |
         |
==========
    """
    ]

words = ['girl', 'boy', 'panda', 'hang', 'office']
chosen_word = random.choice(words)


# show spaces as the same len for the random word
spaces = ['_' for _ in chosen_word]

print(' '.join(spaces))
print("""
    +---+
         |
         |
         |
         |
         |
==========
    """)


lives = 6
# list for the same guessed letter
guessed_letters = []


while "_" in spaces and lives > 0:
    # ask the user to guess a letter
    guessed = input('Guess a letter: ').lower()
    
    # check if the letter is unique?
    if guessed in guessed_letters:
        print("You've already guessed that letter. Try again.")
        continue
    # if not gussed before, add it to the guessed letters
    guessed_letters.append(guessed)

    # if correct replace teh space with the letter
    if guessed in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guessed:
                spaces[position] = guessed
        print("".join(spaces))
        
    # if wrong, then show wrong tries and try again
    
    else:
        lives -= 1
        print(f"That is wrong, you got {lives} tries left!")
        print(hangman_stages[lives])
        if lives == 0:
            print(f"The correct word is: {chosen_word}\n")


if '_' not in spaces:
    print("""
    ###############
    Tadada, YOU WIN
    ###############
    """)
