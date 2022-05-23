import random

number = random.randint(1,100)
print('We picked a number from 1 to 100')
inputres = input('Make a guess: ')
if(inputres == ''):
  inputres = number
guess = int(inputres)
guesses = [] 
guesses.append(guess)

while guess != number:
  if guess > 100 or guess < 1:
    print('OUT OF BOUNDS')
    pass
  elif len(guesses) >= 2:
    if abs(number - guesses[-2]) < abs(number - guesses[-1]):
      print('COLDER')
    elif abs(number - guesses[-2]) > abs(number -   guesses[-1]):
      print('WARMER')
  else: 
    if abs(number - guess <= 10):
      print('WARM')
    elif abs(number - guess > 10):
      print('COLD')
  inputres = input('Make a guess: ')
  if(inputres == ''):
    inputres = number
  guess = int(inputres)
  guesses.append(guess)
print(number, guess)