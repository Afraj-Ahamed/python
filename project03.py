import random
import hangman

words = ["apple","banana","python","afraj"]
lives = 6
random_word = random.choice(words)
display = []
for i in range(len(random_word)):
    display += '_'
print(display)

game_over  = False
while not game_over:
    guessed_letter = input("guess a letter :").lower()
    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)
    if guessed_letter not in random_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lose !")
    if '_' not in display:
        game_over = True
        print("you win")
    print(hangman.hangman_stages[lives])

else:
    print("now game is finished")

