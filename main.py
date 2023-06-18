import random
import hangman_words

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')
lives = 6
# - Create an empty List called display.
display = []

for x in chosen_word:
    display.append("_")

end_game = False
while end_game == False and lives >= 0:
    guess = input("Guess a letter: ").lower()
    found_letter = False
    counter = 0
    for letter in chosen_word:
        if letter == guess:
            display[counter] = letter
            found_letter = True
        counter += 1

    if found_letter == False:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        print(stages[lives])
        print(f"{' '.join(display)}")
        lives -= 1
    else:
        print(f"You've already guessed {guess}")
        print(f"{' '.join(display)}")

    if "_" not in display:
        end_game = True
if end_game or lives >= 0:
    print("You win")
else:
    print("You lose")
print(f"The word was {chosen_word}")
