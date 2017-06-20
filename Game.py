import random
attempts = 0
number = random.randint(1, 2000)
print('Hello! I am thinking of a number between 1 and 2000, can you guess what it is?')
while attempts >= 0: 
  guess = input()
  guess = int(guess)
  attempts = attempts + 1
  if guess < number:
    print ('Go higher')
    guess = int(guess)
  if guess > number:
    print ('Too high!')
  if guess == number:
    attempts = str(attempts)
    print ("In " + attempts + " tries, you guessed the number!")
    break
 
