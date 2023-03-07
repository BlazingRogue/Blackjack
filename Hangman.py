import random
import course

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

word_list = course.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
letters = []
#print(f'Solution is {chosen_word}')

for length in chosen_word:
    display.append('_')
#for length in range(len(chosen_word)): display += "_"


end_of_game = False
lives = 6

while not end_of_game:

    guess = input('Pick a letter: ').lower()
    letters += (guess)
    for position in range(word_length):
        letter = chosen_word[position]
        if letter in guess:
            display[position] = f'{letter}'
        if guess not in chosen_word:
            lives += -1
            break # you could write the if statement outside of the for loop as well

    if '_' not in display:
        end_of_game = True
        print(f'The word was {"".join(display)}')
        print('You won!')
        break
    if lives <= 0:
        end_of_game = True
        print("You lost!")
        print(f'The word was {chosen_word}')
    if lives > 0:
        print(f'{" ".join(display)}')
        print(f'You have {lives} lives left.')
        print(f'Guessed: {" ".join(letters)}')
    print(stages[lives])
