import random

num = 0


def generate_random_number(lower_bound, upper_bound):
  rand_num = random.randint(lower_bound, upper_bound)
  print(rand_num)


def difference_from_answer(guess, answer):
  if guess > answer:
    print("Too high")
  elif guess < answer:
    print("Too Low")
  else:
    print("Correct")
