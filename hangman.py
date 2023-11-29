import random
import hangman_stages
word_list=["apple","beautiful","potato"]
chosen_word=random.choice(word_list)
print(chosen_word)
lives=6
display=[]
for i in range(len(chosen_word)):
   display +='_'
print(display)
game_over=False
while not game_over:
  guessed_letter=input("Guess a letter: ").lower()
  for positon in range(len(chosen_word)):
    letter=chosen_word[positon]
    if letter==guessed_letter:
      display[positon]=guessed_letter
  print(display)
  if guessed_letter not in chosen_word:
     lives-=1
     if lives==0:
       game_over=True
       print("you lose")
  if '_' not in display:
    game_over=True
    print('you win')
  print(hangman_stages.stages[lives])