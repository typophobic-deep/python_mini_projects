import random

num = random.randint(1, 100)
print(num)

guesses = [0]
guess_limit = 0
while True:
  guess = int(input("enter you guess : "))
  if guess_limit < 9:
    if guess < 1 or guess > 100:
      print("OUT OF BOUNDS")
      continue
    if num == guess:
      print("congrats u guessed it in {0} chances".format(len(guesses)))
      break
    guesses += [guess]
    guess_limit += 1

    if len(guesses) == 2:
      if abs(guess - num <= 10):
        print("warm, 9 chances left")
      else:
        print("cold, 9 chances left")

    else:
      if abs(guess - num) < abs(guesses[-2] - num):
        print("warmer ,chances left ", (11 - len(guesses)))
      else:
        print("colder,chances left", (11 - len(guesses)))
  else:
    print("limit exceeded , the number was ", num)
    break
