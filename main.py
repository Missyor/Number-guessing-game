###Create a guessing game
## the # symbol causes the computer to skip over the comment

import random ##imports the random module - needed for computer to choose a random number

## Create a variable that will store a random number between 1 and 10.
number = random.randint(1, 10) 

##See the number so you can test your code
print(number)

#Create a variable that stores the persons name
name = input("Hi, please enter your name: ")

##Print a greeting for the player using their name
print("Hi", name, "play my guessing game")

## Create a variable that allows the user to enter a number. int means the computer will recognise the guess as a number.
guess = int(input("Enter a number between 1 and 10: "))

## If the user enters a guess that is the same as the number the computer says "Correct! The number was..." or whatever or else the computer says "hard luck".
if guess == number:
  print("Correct! The number was", number)
else:
  print("Hard luck!")  

#############################
'''
Improve your code by stating that if the guess is greater than the number, print "your guess is too high! The answer is..." or else if the guess is less than the number print "your guess is too low! The answer is ...". 
Keep the code: 
if guess == number:
  print("Correct! The number was", number)
else:
  print("Hard luck!") 
'''



#### Improve your code
## If the person guesses the wrong number they should be asked if they want to play again. If they choose yes, let them play again
