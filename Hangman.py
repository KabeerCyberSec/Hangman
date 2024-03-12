import random
HANGMANSTAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']
words = ['able', 'about', 'account', 'acid', 'across', 'act', 'addition', 'adjustment', 'advertisement', 'after', 'again', 'against', 'agreement', 'air', 'all', 'almost', 'among', 'amount', 'amusement', 'and', 'angle', 'angry', 'animal', 'answer', 'ant', 'any', 'apparatus', 'apple', 'approval', 'arch', 'argument', 'arm', 'army', 'art', 'as', 'at', 'attack', 'attempt', 'attention', 'attraction', 'authority', 'automatic', 'awake', 'baby', 'back', 'bad', 'bag', 'balance', 'ball', 'band', 'base', 'basin', 'basket', 'bath', 'be', 'beautiful', 'because', 'bed', 'bee', 'before', 'behaviour', 'belief', 'bell', 'bent', 'berry', 'between', 'bird', 'birth', 'bit', 'bite', 'bitter', 'black', 'blade', 'blood', 'blow', 'blue', 'board', 'boat', 'body', 'boiling', 'bone', 'book', 'boot', 'bottle', 'box', 'boy', 'brain', 'brake', 'branch', 'brass', 'bread', 'breath', 'brick', 'bridge', 'bright', 'broken', 'brother', 'brown', 'brush', 'bucket', 'building', 'bulb', 'burn', 'burst', 'business', 'but', 'butter', 'button', 'by', 'cake', 'camera', 'canvas', 'card', 'care', 'carriage', 'cart', 'cat', 'cause', 'certain', 'chain', 'chalk', 'chance', 'change', 'cheap', 'cheese', 'chemical', 'chest', 'chief', 'chin', 'church', 'circle', 'clean', 'clear', 'clock', 'cloth', 'cloud', 'coal', 'coat', 'cold', 'collar', 'colour', 'comb', 'come', 'comfort', 'committee', 'common', 'company', 'comparison', 'competition', 'complete', 'complex', 'condition', 'connection', 'conscious', 'control', 'cook', 'copper', 'copy', 'cord', 'cork', 'cotton', 'cough', 'country', 'cover', 'cow', 'crack', 'credit', 'crime', 'cruel', 'cruel', 'alphabay','blackmarket','darknet']
choosen_word = random.choice(words)
length = len(choosen_word)
life = 6
display_words = []
name = input("What is Your Name: ")
print(f"Welcome To Our Classic Game Hangman Mr.{name}")
for index in range(length):
    display_words += "_"
position = 0
while life:
    print(HANGMANSTAGES[6-life])
    guess = input("Guess the Word :        " + ' '.join(display_words) + f"\n\nEnter your Guess Mr.{name}: ").lower()
    if guess not in choosen_word:
        life -= 1
    else:
        for alpha in choosen_word:
            if guess == alpha and guess != display_words[position]:
                display_words[position] = guess
                break
            else:
                position += 1
                if position == len(choosen_word):
                    life -= 1
        position = 0
    if "_" not in display_words:
        print(HANGMANSTAGES[6 - life])
        print(f"Guess the Word :        " + ' '.join(display_words))
        print(f"Congratulations Mr.{name}! You Guessed & Have Saved Your Hangman :)")
        life = 0
    elif life <= 0:
        print(HANGMANSTAGES[6-life])
        print(f"We are Sorry Mr.{name}. Hangman Has Died Due To Dipression & Insufficiant Oxygen :(")
        print("Word was : " + choosen_word)
