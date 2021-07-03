#AmrMuallaGUESSINGGAMESHOW.
import random
from art import logo
def GuessingGame():
  print(logo)
  print("Welcome to Amr's Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100 ")
  difficulty = input("Choose a difficulty, easy or hard? Type 'easy' or 'hard': ")

  randomnum = random.randint(1, 101)
  if difficulty == "easy":
    attempts = 10
  elif difficulty == "hard":
    attempts = 5

  print(f"You have {attempts} attempts remaining to guess the number. ")

  while attempts > 0:
    Guess = int(input("Make a guess: "))
    if Guess == randomnum:
      print(f"You win! The number was {randomnum}. ")
    elif Guess < randomnum:
      print("Too Low")
      attempts = attempts - 1
      print(f"You have {attempts} attempts remaining to guess the number. ")
    elif Guess > randomnum:
      print("Too High")
      attempts = attempts - 1
      print(f"You have {attempts} attempts remaining to guess the number. ")

  if attempts == 0:
    Again = input(f"You lose. The number was {randomnum} Would you like to play again? Press Y for Yes and N for No. ")
    if(Again == 'Y'):
      GuessingGame()
  
GuessingGame()


